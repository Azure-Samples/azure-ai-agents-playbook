# Orchestrated Agents with Custom OpenAPI Tools

Learn how to connect Azure AI Agents to your own custom FastAPI services. Build agents that understand and interact with your business data through standardized OpenAPI specifications.

## What You'll Learn

- Create RESTful APIs with FastAPI and automatic OpenAPI spec generation
- Connect agents to custom APIs using OpenAPI tools
- Deploy services locally and to Azure Container Apps
- Build agents that work with real business data (banking transactions)

## Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Azure AI      │    │   Custom FastAPI │    │   Azure         │
│   Agents        │◄──►│   Service        │    │   Container     │
│                 │    │                  │    │   Apps          │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

![SK Orchestration](images/sk_orchestration.gif)

## Project Structure

```
05-orchestrated-agents-with-custom-openapi-tools/
├── 05.1-fastapi_openapi_tutorial.ipynb    # Main tutorial notebook
├── bank_transactions_api.py                # FastAPI service implementation
├── Dockerfile                             # Container configuration
├── aci_requirements.txt                   # Python dependencies
├── azure.yaml                            # Azure Developer CLI configuration
├── infra/                                # Infrastructure as Code
└── arm/                                  # ARM template for one-click deploy
```
│       └── uami.bicep                   # User Assigned Managed Identity
└── arm/                                  # ARM template for one-click deploy
    └── main.json                        # ARM template
```

## Quick Start

### Option 1: One-Click Azure Deployment

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FAzure-Samples%2Fazure-ai-agents-playbook%2Fmain%2F05-orchestrated-agents-with-custom-openapi-tools%2Farm%2Fmain.json)

### Option 2: Azure Developer CLI

```bash
# Clone and deploy
git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
cd azure-ai-agents-playbook/05-orchestrated-agents-with-custom-openapi-tools
azd up
```

### Option 3: Local Development

```bash
# Install dependencies and run locally
pip install -r aci_requirements.txt
python bank_transactions_api.py 8000

# In another terminal
jupyter notebook 05.1-fastapi_openapi_tutorial.ipynb
```
   - Create a new resource group
   - Deploy Azure Container Registry
   - Set up Azure Container Apps Environment
   - Deploy Log Analytics workspace for monitoring## Prerequisites

### Azure Resources
- Azure AI Project with deployed language model
- Azure subscription with appropriate permissions

### Environment Variables
Set these in your `.env` file at the project root:

```properties
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="gpt-4o"  # or your deployed model name
```

### Required Python Packages
```bash
pip install azure-ai-agents azure-identity semantic-kernel fastapi uvicorn requests python-dotenv
```

## Features

### Bank Transactions API
- `GET /transactions` - Retrieve latest bank transactions
- `GET /transactions/{id}` - Get specific transaction details
- `GET /openapi.json` - OpenAPI specification endpoint
- `GET /docs` - Interactive API documentation

### Azure AI Agent Capabilities
- Connect to FastAPI endpoints using OpenAPI specifications
- Ask natural language questions about financial data
- Get insights, summaries, and categorized spending analysis
- Work with real-time data from live API endpoints

## Tutorial Walkthrough

The `05.1-fastapi_openapi_tutorial.ipynb` notebook covers:

1. **Setup and Prerequisites** - Environment configuration
2. **Start FastAPI Service** - Launch the bank transactions API
3. **Test API Endpoints** - Verify the service works correctly
4. **Fetch OpenAPI Spec** - Retrieve the API specification
5. **Create Azure AI Agent** - Build an agent with OpenAPI tools
6. **Interactive Testing** - Query the agent with natural language

## Example Use Cases

**Financial Assistant queries:**
- "Show me my latest bank transactions and how much I spent on food"
- "What was my largest expense recently and what category was it?"
- "Give me a summary of my account balance and recent activity"

**Integration Patterns:**
- Connect agents to existing business APIs
- Enable conversational queries over structured data
- Create workflow automation with business processes
- Build real-time monitoring and reporting systems

## Next Steps

After completing this tutorial:
- [06-magentic-one-orchestration](../06-magentic-one-orchestration/) - Advanced orchestration patterns
- [07-voice-orchestration](../07-voice-orchestration/) - Voice-enabled agents