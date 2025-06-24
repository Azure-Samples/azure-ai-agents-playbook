# Agent Basics

This folder covers the fundamentals of Azure AI Agents. Start here if you're new to the platform.

## What's In This Folder

**[01.1 - Azure AI Agents Foundry SDK Tutorial](01.1-azure_ai_agents_foundry_sdk_tutorial.ipynb)**
Your first Azure AI Agent using Microsoft's official SDK. Learn how to create agents, manage conversations, and handle multi-turn discussions.

![Single Agent](images/single_agent.gif)

**[01.2 - Semantic Kernel Tutorial](01.2-azure_ai_agents_semantic_kernel_tutorial.ipynb)**
Build more sophisticated agents using Semantic Kernel's orchestration features. Add plugins, handle async operations, and create reusable components.

![Single Agent with SK Wrapper](images/single_agent_with_sk.gif)

**[01.3 - Python `with` Statement Tutorial](01.3-python_with_statement_agents_tutorial.ipynb)**
Learn proper resource management patterns. This tutorial covers when to use `with` statements and how to write cleaner, more reliable code.

## Learning Path

1. Start with **01.1** to understand the basics
2. Move to **01.2** for more advanced features
3. Complete **01.3** to learn best practices

## Prerequisites

### Azure Resources
- Azure subscription
- Azure AI Foundry project
- Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)

### Environment Setup
- Python 3.8+
- Jupyter Notebook or VS Code
- Azure CLI (optional)

### Environment Variables
Configure your Azure AI services in the `.env` file at the project root:

```bash
# Navigate to the project root and edit the .env file
cd ../../  # Go to azure-ai-agents-playbook root
```

Update the `.env` file with your Azure AI project details:
```properties
# Required for all tutorials
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="your-model-deployment-name"

# For Semantic Kernel scenarios
AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
AZURE_OPENAI_ENDPOINT="https://your-openai-resource.openai.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your-chat-deployment"
AZURE_OPENAI_DEPLOYMENT_NAME="your-deployment-name"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Optional: For advanced scenarios
AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

**Tip**: The `.env` file already exists in the project root with example values - just update it with your details.

### Required Packages
Install the packages you need:

```bash
pip install azure-ai-agents azure-identity semantic-kernel
```

## What You'll Learn

By completing these tutorials, you'll understand:

- How to create and manage Azure AI Agents
- The difference between Foundry SDK and Semantic Kernel approaches
- Conversation management with threads and context
- Proper resource management with Python context managers
- Best practices for agent development

## Next Steps

After finishing the basics, check out:
- [02-agent-custom-functions](../02-agent-custom-functions/) - Add custom capabilities
- [03-orchestrated-agents](../03-orchestrated-agents/) - Coordinate multiple agents
