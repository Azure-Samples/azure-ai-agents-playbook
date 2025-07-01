# Agent Custom Functions

Learn how to extend your agents with custom functions and plugins. This is where your agents become truly useful by connecting to external services and performing real tasks.

## What's In This Folder

**[02.1 - Azure AI Agents Functions (Foundry SDK)](02.1-azure_ai_agents_functions_foundry_sdk_tutorial.ipynb)**
Add custom functions to your agents using the official Azure AI Agents SDK. Build calculators, weather tools, and data processors that your agents can use.

**[02.2 - Semantic Kernel Plugins](02.2-azure_ai_agents_semantic_kernel_plugins_tutorial.ipynb)**
Create sophisticated plugins using Semantic Kernel's decorator system. Learn type-safe development and build reusable plugin libraries.

![SK Plugins](images/sk_plugins.gif)


## Learning Path

1. **Start with 02.1** - Learn function basics with the Foundry SDK
2. **Move to 02.2** - Explore advanced plugin architecture

**Prerequisites**: Complete [01-agent-basics](../01-agent-basics/) first.

## Prerequisites

### Previous Knowledge
- Complete [01-agent-basics](../01-agent-basics/) tutorials
- Basic Python programming

### Azure Resources
- Azure subscription
- Azure AI Foundry project
- Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)

### Environment Setup
- Python 3.8+
- Jupyter Notebook or VS Code

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
pip install azure-ai-agents azure-identity semantic-kernel requests
```

## What You'll Learn

### Function Types
- **Foundry SDK Functions**: Direct function registration with fine-grained control
- **Semantic Kernel Plugins**: Automatic function discovery with type safety


## Next Steps

After mastering functions and plugins:
- [03-orchestrated-agents](../03-orchestrated-agents/) - Coordinate multiple agents
- [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/) - Advanced tool integration
