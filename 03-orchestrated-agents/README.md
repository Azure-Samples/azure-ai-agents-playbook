# Orchestrated Agents

Learn how to coordinate multiple agents to solve complex problems. This is where individual agents become a powerful team.

## What's In This Folder

**[03.1 - Concurrent and Sequential Orchestration](03.1-concurrent_and_sequential_orchestration_tutorial.ipynb)**
Master different orchestration patterns using Semantic Kernel. Build specialized agent teams that work in pipelines or in parallel to handle complex tasks.

**Sequential Orchestration**: Agents work in a pipeline (Agent A → Agent B → Agent C)
![Sequential Orchestration](images/sequential_orchestration.gif)

**Concurrent Orchestration**: Agents work in parallel (A + B + C → Combine)
![Concurrent Orchestration](images/concurrent_orchestration.gif)

**[03.2 - Connected Agents](03.2-connected_agents_tutorial.ipynb)**
Learn different approaches to agent communication. Compare Azure AI Foundry's ConnectedAgentTool with Semantic Kernel's AzureAIAgent plugins.

![Connected Agents](images/connected_agents.gif)

## Learning Path

1. **Start with 03.1** - Master orchestration patterns with specialized teams
2. **Move to 03.2** - Learn agent connectivity approaches

**Prerequisites**: Complete [01-agent-basics](../01-agent-basics/) and [02-agent-custom-functions](../02-agent-custom-functions/).

## Prerequisites

### Previous Knowledge
- Complete [01-agent-basics](../01-agent-basics/) and [02-agent-custom-functions](../02-agent-custom-functions/) tutorials
- Understanding of async/await patterns in Python

### Azure Resources
- Azure subscription
- Azure AI Foundry project
- Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)
- Azure OpenAI resource (for Semantic Kernel scenarios)

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

# Required for Semantic Kernel orchestration (03.1)
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
pip install azure-ai-agents azure-identity semantic-kernel python-dotenv
```

## What You'll Learn

### Orchestration Patterns

**Sequential Orchestration (Pipeline)**
- Flow: Agent A → Agent B → Agent C
- Best for: Document processing, analysis workflows, step-by-step procedures
- Example: Research Agent → Analytics Agent → Content Agent

**Concurrent Orchestration (Parallel)**
- Flow: Agent A + Agent B + Agent C → Combine Results
- Best for: Independent tasks, multi-source research, parallel processing
- Example: Multiple research agents gathering different data sources

**Hybrid Patterns**
- Mix of sequential and concurrent patterns for complex workflows

### Agent Connectivity

**Connected Agents (Foundry SDK)**
- Use ConnectedAgentTool for agent-to-agent communication
- Direct delegation and simple coordination

**AzureAI Plugins (Semantic Kernel)**
- Wrap Azure AI agents as Semantic Kernel plugins
- Rich orchestration features and advanced patterns

### What You'll Build
- Research + Analytics + Content Pipeline (sequential workflow)
- Multi-Perspective Analysis System (concurrent agents)
- Specialized Agent Network (domain experts working together)

## Next Steps

After mastering orchestration:
- [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/) - External API integration
- [05-orchestrated-agents-with-custom-openapi-tools](../05-orchestrated-agents-with-custom-openapi-tools/) - Custom API services
