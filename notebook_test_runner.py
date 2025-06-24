#!/usr/bin/env python3
"""
Notebook Test Runner for CI/CD Pipeline

This script executes all Jupyter notebooks in the workspace and tracks their
success/failure status. It's designed to be the first piece in a CI/CD pipeline
that can be triggered nightly with GitHub Actions.

Usage:
    python notebook_test_runner.py [--timeout SECONDS] [--output-format FORMAT]

The script will:
1. Discover all .ipynb files in the workspace
2. Execute each notebook in order
3. Track execution time and success/failure status
4. Generate a detailed report
5. Exit with appropriate status code for CI/CD integration
"""

import argparse
import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors.execute import CellExecutionError


class NotebookTestRunner:
    """Main class for running notebook tests."""
    
    def __init__(self, timeout: int = 600, output_format: str = "console"):
        """
        Initialize the notebook test runner.
        
        Args:
            timeout: Maximum time in seconds to wait for each notebook to complete
            output_format: Output format for results ("console", "json", "html")
        """
        self.timeout = timeout
        self.output_format = output_format
        self.results = []
        self.start_time = datetime.now()
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('notebook_test_runner.log'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def discover_notebooks(self, root_path: str = ".") -> List[Path]:
        """
        Discover all Jupyter notebooks in the workspace.
        
        Args:
            root_path: Root path to search for notebooks
            
        Returns:
            List of notebook file paths
        """
        notebook_paths = []
        root = Path(root_path).resolve()
        
        # Find all .ipynb files, excluding checkpoints and build directories
        for notebook_path in root.rglob("*.ipynb"):
            # Skip checkpoint files and build directories
            if ".ipynb_checkpoints" in str(notebook_path):
                continue
            if "build" in notebook_path.parts:
                continue
            
            notebook_paths.append(notebook_path)
        
        # Sort notebooks by path for consistent execution order
        notebook_paths.sort()
        
        self.logger.info(f"Discovered {len(notebook_paths)} notebooks")
        for nb_path in notebook_paths:
            self.logger.info(f"  - {nb_path.relative_to(root)}")
        
        return notebook_paths
    
    def execute_notebook(self, notebook_path: Path) -> Dict:
        """
        Execute a single notebook and return execution results.
        
        Args:
            notebook_path: Path to the notebook file
            
        Returns:
            Dictionary containing execution results
        """
        result = {
            "notebook": str(notebook_path.relative_to(Path.cwd())),
            "status": "unknown",
            "execution_time": 0,
            "start_time": datetime.now().isoformat(),
            "end_time": None,
            "error_message": None,
            "cells_executed": 0,
            "total_cells": 0
        }
        
        start_time = time.time()
        
        try:
            self.logger.info(f"Executing notebook: {result['notebook']}")
            
            # Read the notebook
            with open(notebook_path, "r", encoding="utf-8") as f:
                notebook = nbformat.read(f, as_version=4)
            
            # Count total cells
            result["total_cells"] = len([cell for cell in notebook.cells if cell.cell_type == "code"])
            
            # Create executor
            executor = ExecutePreprocessor(
                timeout=self.timeout,
                kernel_name="python3",
                allow_errors=False  # Stop on first error
            )
            
            # Execute the notebook
            executor.preprocess(notebook, {"metadata": {"path": str(notebook_path.parent)}})
            
            # Count executed cells
            result["cells_executed"] = len([
                cell for cell in notebook.cells 
                if cell.cell_type == "code" and cell.get("execution_count") is not None
            ])
            
            result["status"] = "success"
            self.logger.info(f"✅ Successfully executed: {result['notebook']}")
            
        except CellExecutionError as e:
            result["status"] = "failed"
            result["error_message"] = str(e)
            self.logger.error(f"❌ Cell execution error in {result['notebook']}: {e}")
            
        except Exception as e:
            result["status"] = "error"
            result["error_message"] = str(e)
            self.logger.error(f"💥 Unexpected error in {result['notebook']}: {e}")
        
        finally:
            end_time = time.time()
            result["execution_time"] = round(end_time - start_time, 2)
            result["end_time"] = datetime.now().isoformat()
        
        return result
    
    def run_all_notebooks(self, root_path: str = ".") -> List[Dict]:
        """
        Run all discovered notebooks and return results.
        
        Args:
            root_path: Root path to search for notebooks
            
        Returns:
            List of execution results for each notebook
        """
        notebooks = self.discover_notebooks(root_path)
        
        if not notebooks:
            self.logger.warning("No notebooks found to execute")
            return []
        
        self.logger.info(f"Starting execution of {len(notebooks)} notebooks")
        
        for notebook_path in notebooks:
            result = self.execute_notebook(notebook_path)
            self.results.append(result)
            
            # Add some spacing between notebook executions
            time.sleep(1)
        
        return self.results
    
    def generate_summary(self) -> Dict:
        """Generate a summary of all test results."""
        if not self.results:
            return {
                "total_notebooks": 0,
                "successful": 0,
                "failed": 0,
                "errors": 0,
                "total_execution_time": 0,
                "overall_status": "no_notebooks"
            }
        
        successful = len([r for r in self.results if r["status"] == "success"])
        failed = len([r for r in self.results if r["status"] == "failed"])
        errors = len([r for r in self.results if r["status"] == "error"])
        total_time = sum(r["execution_time"] for r in self.results)
        
        overall_status = "success" if failed == 0 and errors == 0 else "failed"
        
        return {
            "total_notebooks": len(self.results),
            "successful": successful,
            "failed": failed,
            "errors": errors,
            "total_execution_time": round(total_time, 2),
            "overall_status": overall_status,
            "test_run_start": self.start_time.isoformat(),
            "test_run_end": datetime.now().isoformat()
        }
    
    def output_results(self):
        """Output results in the specified format."""
        summary = self.generate_summary()
        
        if self.output_format == "json":
            self._output_json(summary)
        elif self.output_format == "html":
            self._output_html(summary)
        else:
            self._output_console(summary)
    
    def _output_console(self, summary: Dict):
        """Output results to console in a human-readable format."""
        print("\n" + "="*80)
        print("📊 NOTEBOOK TEST RUNNER RESULTS")
        print("="*80)
        
        print(f"📝 Total notebooks: {summary['total_notebooks']}")
        print(f"✅ Successful: {summary['successful']}")
        print(f"❌ Failed: {summary['failed']}")
        print(f"💥 Errors: {summary['errors']}")
        print(f"⏱️  Total execution time: {summary['total_execution_time']} seconds")
        print(f"🎯 Overall status: {summary['overall_status'].upper()}")
        
        print("\n📋 DETAILED RESULTS:")
        print("-" * 80)
        
        for result in self.results:
            status_icon = "✅" if result["status"] == "success" else "❌" if result["status"] == "failed" else "💥"
            print(f"{status_icon} {result['notebook']}")
            print(f"   Status: {result['status']}")
            print(f"   Execution time: {result['execution_time']}s")
            print(f"   Cells executed: {result['cells_executed']}/{result['total_cells']}")
            
            if result["error_message"]:
                print(f"   Error: {result['error_message'][:100]}...")
            print()
    
    def _output_json(self, summary: Dict):
        """Output results in JSON format."""
        output = {
            "summary": summary,
            "results": self.results
        }
        
        with open("notebook_test_results.json", "w") as f:
            json.dump(output, f, indent=2)
        
        print(json.dumps(output, indent=2))
    
    def _output_html(self, summary: Dict):
        """Output results in HTML format."""
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Notebook Test Results</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .summary {{ background: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
        .success {{ color: green; }}
        .failed {{ color: red; }}
        .error {{ color: orange; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
    </style>
</head>
<body>
    <h1>📊 Notebook Test Results</h1>
    
    <div class="summary">
        <h2>Summary</h2>
        <p><strong>Total notebooks:</strong> {summary['total_notebooks']}</p>
        <p><strong>Successful:</strong> <span class="success">{summary['successful']}</span></p>
        <p><strong>Failed:</strong> <span class="failed">{summary['failed']}</span></p>
        <p><strong>Errors:</strong> <span class="error">{summary['errors']}</span></p>
        <p><strong>Total execution time:</strong> {summary['total_execution_time']} seconds</p>
        <p><strong>Overall status:</strong> {summary['overall_status'].upper()}</p>
    </div>
    
    <h2>Detailed Results</h2>
    <table>
        <tr>
            <th>Notebook</th>
            <th>Status</th>
            <th>Execution Time (s)</th>
            <th>Cells Executed</th>
            <th>Error Message</th>
        </tr>
"""
        
        for result in self.results:
            status_class = result["status"]
            error_msg = result["error_message"][:100] + "..." if result["error_message"] else ""
            
            html_content += f"""
        <tr>
            <td>{result['notebook']}</td>
            <td class="{status_class}">{result['status']}</td>
            <td>{result['execution_time']}</td>
            <td>{result['cells_executed']}/{result['total_cells']}</td>
            <td>{error_msg}</td>
        </tr>
"""
        
        html_content += """
    </table>
</body>
</html>
"""
        
        with open("notebook_test_results.html", "w") as f:
            f.write(html_content)
        
        print("HTML report generated: notebook_test_results.html")
    
    def get_exit_code(self) -> int:
        """Get appropriate exit code for CI/CD systems."""
        summary = self.generate_summary()
        
        if summary["overall_status"] == "success":
            return 0  # Success
        elif summary["overall_status"] == "no_notebooks":
            return 2  # No notebooks found
        else:
            return 1  # Failures or errors


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Execute Jupyter notebooks and generate test reports for CI/CD pipelines"
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Maximum time in seconds to wait for each notebook (default: 600)"
    )
    parser.add_argument(
        "--output-format",
        choices=["console", "json", "html"],
        default="console",
        help="Output format for results (default: console)"
    )
    parser.add_argument(
        "--root-path",
        default=".",
        help="Root path to search for notebooks (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Create and run the test runner
    runner = NotebookTestRunner(
        timeout=args.timeout,
        output_format=args.output_format
    )
    
    try:
        runner.run_all_notebooks(args.root_path)
        runner.output_results()
        exit_code = runner.get_exit_code()
        
        if exit_code == 0:
            runner.logger.info("🎉 All notebooks executed successfully!")
        elif exit_code == 1:
            runner.logger.error("❌ Some notebooks failed to execute")
        else:
            runner.logger.warning("⚠️  No notebooks found to execute")
        
        sys.exit(exit_code)
        
    except KeyboardInterrupt:
        runner.logger.info("🛑 Test run interrupted by user")
        sys.exit(130)
    except Exception as e:
        runner.logger.error(f"💥 Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
