# Notebook Test Runner

This script executes all Jupyter notebooks in the workspace and tracks their success/failure status. It's designed to be the first piece in a CI/CD pipeline that can be triggered nightly with GitHub Actions.

## Features

- 🔍 **Auto-discovery**: Automatically finds all `.ipynb` files in the workspace
- ⚡ **Parallel execution**: Executes notebooks in a controlled manner
- 📊 **Detailed reporting**: Provides comprehensive execution reports
- 🎯 **CI/CD ready**: Returns appropriate exit codes for automation
- 📝 **Multiple output formats**: Console, JSON, and HTML reports
- ⏱️ **Timeout protection**: Prevents hanging notebooks from blocking the pipeline
- 📋 **Execution tracking**: Tracks cells executed, timing, and error details

## Usage

### Basic Usage

```bash
# Run all notebooks with default settings
python notebook_test_runner.py

# Run with custom timeout (10 minutes)
python notebook_test_runner.py --timeout 600

# Generate JSON report
python notebook_test_runner.py --output-format json

# Generate HTML report
python notebook_test_runner.py --output-format html
```

### Command Line Options

- `--timeout SECONDS`: Maximum time to wait for each notebook (default: 600 seconds)
- `--output-format FORMAT`: Output format - `console`, `json`, or `html` (default: console)
- `--root-path PATH`: Root path to search for notebooks (default: current directory)

## Output Formats

### Console Output
Human-readable summary with status icons and detailed results.

### JSON Output
Machine-readable format perfect for CI/CD integration. Creates `notebook_test_results.json`.

### HTML Output
Beautiful HTML report with styling. Creates `notebook_test_results.html`.

## Exit Codes

- `0`: All notebooks executed successfully
- `1`: Some notebooks failed or had errors
- `2`: No notebooks found to execute
- `130`: Interrupted by user (Ctrl+C)

## CI/CD Integration

The script is designed for CI/CD pipelines. It will:

1. Return appropriate exit codes
2. Generate detailed logs
3. Create test artifacts (JSON/HTML reports)
4. Handle timeouts gracefully
5. Skip problematic files (checkpoints, build directories)

## Example GitHub Actions Integration

```yaml
name: Nightly Notebook Tests

on:
  schedule:
    - cron: '0 2 * * *'  # Run at 2 AM daily
  workflow_dispatch:      # Allow manual triggers

jobs:
  test-notebooks:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run notebook tests
      run: |
        python notebook_test_runner.py --output-format json --timeout 900
    
    - name: Upload test results
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: notebook-test-results
        path: |
          notebook_test_results.json
          notebook_test_runner.log
```

## Logs

The script generates detailed logs in `notebook_test_runner.log` with timestamps and execution details.

## Discovered Notebooks

The script will automatically discover and execute these notebooks:

- `01-agent-basics/01.1-azure_ai_agents_foundry_sdk_tutorial.ipynb`
- `01-agent-basics/01.2-azure_ai_agents_semantic_kernel_tutorial.ipynb`
- `01-agent-basics/01.3-python_with_statement_agents_tutorial.ipynb`
- `02-agent-custom-functions/02.1-azure_ai_agents_functions_foundry_sdk_tutorial.ipynb`
- `02-agent-custom-functions/02.2-azure_ai_agents_semantic_kernel_plugins_tutorial.ipynb`
- `03-orchestrated-agents/03.1-concurrent_and_sequential_orchestration_tutorial.ipynb`
- `03-orchestrated-agents/03.2-connected_agents_tutorial.ipynb`
- `04-orchestrated-agents-with-tools/04.1-openapi_currency_exchange_tutorial.ipynb`
- `04-orchestrated-agents-with-tools/04.2-hybrid_openapi_and_plugins_tutorial.ipynb`
- `04-orchestrated-agents-with-tools/04.3-logic_apps_hybrid_tutorial.ipynb`
- `05-orchestrated-agents-with-custom-openapi-tools/05.1-fastapi_openapi_tutorial.ipynb`
- `06-magentic-one-orchestration/06.1-magentic_creative_writing_tutorial.ipynb`
- `06-magentic-one-orchestration/06.2-magentic_bing_search_orchestration_tutorial.ipynb`

## Error Handling

The script handles various error scenarios:

- **Cell execution errors**: Captures and reports failed cells
- **Timeout errors**: Prevents hanging notebooks
- **Missing dependencies**: Reports import errors
- **File access errors**: Handles permission issues
- **Keyboard interrupts**: Graceful shutdown on Ctrl+C
