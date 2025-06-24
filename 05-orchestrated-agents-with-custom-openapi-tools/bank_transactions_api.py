"""
FastAPI Bank Transactions Service

A simple FastAPI service that provides sample bank transaction data
and exposes its OpenAPI specification at /openapi.json
"""

from fastapi import FastAPI
from typing import List, Dict, Any
from datetime import datetime, timedelta
import random

app = FastAPI(
    title="Bank Transactions API",
    description="Returns sample bank transaction data for demonstration purposes",
    version="1.0.0"
)

# Sample bank transaction data
SAMPLE_TRANSACTIONS = [
    {
        "id": "txn_001",
        "date": "2024-12-01",
        "description": "Grocery Store Purchase",
        "amount": -85.47,
        "balance": 2914.53,
        "category": "Food & Dining"
    },
    {
        "id": "txn_002", 
        "date": "2024-12-02",
        "description": "Salary Deposit",
        "amount": 3500.00,
        "balance": 6414.53,
        "category": "Income"
    },
    {
        "id": "txn_003",
        "date": "2024-12-03", 
        "description": "Gas Station",
        "amount": -45.20,
        "balance": 6369.33,
        "category": "Transportation"
    },
    {
        "id": "txn_004",
        "date": "2024-12-04",
        "description": "Online Shopping",
        "amount": -129.99,
        "balance": 6239.34,
        "category": "Shopping"
    },
    {
        "id": "txn_005",
        "date": "2024-12-05",
        "description": "Coffee Shop",
        "amount": -5.75,
        "balance": 6233.59,
        "category": "Food & Dining"
    }
]

@app.get("/")
async def root():
    """Root endpoint with service information"""
    return {
        "service": "Bank Transactions API",
        "version": "1.0.0",
        "endpoints": {
            "transactions": "/transactions",
            "openapi": "/openapi.json",
            "docs": "/docs"
        }
    }

@app.get("/transactions", response_model=List[Dict[str, Any]])
async def get_latest_transactions(limit: int = 10):
    """
    Get the latest bank transactions
    
    Args:
        limit: Maximum number of transactions to return (default: 10)
    
    Returns:
        List of bank transactions with id, date, description, amount, balance, and category
    """
    # Always return the same sample data for consistency
    return SAMPLE_TRANSACTIONS[:limit]

@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str):
    """
    Get a specific transaction by ID
    
    Args:
        transaction_id: The unique transaction identifier
        
    Returns:
        Transaction details or 404 if not found
    """
    for transaction in SAMPLE_TRANSACTIONS:
        if transaction["id"] == transaction_id:
            return transaction
    
    return {"error": "Transaction not found"}, 404

if __name__ == "__main__":
    import uvicorn
    import sys
    
    # Default port
    port = 8000
    
    # Check if port number is provided as command line argument
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            print(f"🚀 Starting server on port {port}")
        except ValueError:
            print(f"❌ Invalid port number: {sys.argv[1]}. Using default port 8000.")
            port = 8000
    else:
        print(f"🚀 Starting server on default port {port}")
        print(f"💡 Usage: python {sys.argv[0]} <port_number>")
    
    uvicorn.run(app, host="0.0.0.0", port=port)
