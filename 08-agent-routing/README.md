# Agent Routing

Learn how to build intelligent agent hierarchies where router agents coordinate multiple specialized agents. Create systems that automatically route complex queries to the right expert agents for optimal responses.

## What's In This Folder

**[08.1 - Azure AI Agent Routing Tutorial](08.1-azure_ai_agent_routing_tutorial.ipynb)**
Complete guide to building hierarchical agent systems with intelligent routing. Learn to create specialized AzureAIAgent workers, build ChatCompletionAgent routers, and coordinate multi-domain queries.

![Agent Router](images/router.gif)

**[plugins.py](plugins.py)**
Comprehensive plugin library with ready-to-use plugins for weather, text analysis, date/time operations, and more business domains.

## Learning Objectives

### Agent Architecture Patterns
- **Base Layer**: Specialized AzureAIAgent workers with persistent state
- **Orchestration Layer**: Lightweight ChatCompletionAgent routers
- **Plugin Integration**: Wrapper patterns for cross-agent communication
- **Hierarchical Organization**: Multi-level agent coordination

### Intelligent Routing Strategies
- **Domain Analysis**: Automatic query classification and routing
- **Specialist Dispatch**: Connecting queries to the right expert agent
- **Multi-Agent Coordination**: Handling queries requiring multiple specialists
- **Fallback Patterns**: Graceful handling of routing edge cases

## Prerequisites

### Azure Resources
- Azure subscription with sufficient quota
- Azure AI Foundry project configured
- Multiple deployed AI models (for different agent types)
- Appropriate permissions for agent creation and management

### Development Environment
- Python 3.8+
- Jupyter Notebook or VS Code
- Understanding of async/await patterns
- Familiarity with Azure AI Agents basics

### Required Knowledge
Complete these tutorials first:
- **[01-agent-basics](../01-agent-basics/)** - Azure AI Agents fundamentals
- **[02-agent-custom-functions](../02-agent-custom-functions/)** - Working with plugins
- **[03-orchestrated-agents](../03-orchestrated-agents/)** - Basic coordination patterns

### Environment Configuration
Update your `.env` file in the project root with:

```properties
# Required for agent routing
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="your-model-deployment-name"

# For Semantic Kernel components
AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
AZURE_OPENAI_ENDPOINT="https://your-openai-resource.openai.azure.com/"
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your-chat-deployment"
AZURE_OPENAI_DEPLOYMENT_NAME="your-deployment-name"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"

# Optional: For advanced scenarios
AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

### Required Packages
Install the necessary packages:

```bash
pip install azure-ai-agents azure-identity semantic-kernel pydantic
```

## Architecture Overview

### The Routing Pattern

```
┌─────────────────────────────┐
│    Orchestration Layer      │  ← ChatCompletionAgent (Router)
│      (Router Agent)         │    • Fast routing decisions
└────────────┬────────────────┘    • Lightweight & stateless
             │                     • Query analysis & dispatch
     ┌───────┼───────┐
     │               │
┌────▼────┐     ┌────▼────┐
│  Base   │     │  Base   │        ← AzureAIAgent (Specialists)
│ Agent 1 │     │ Agent 2 │          • Domain expertise
│Insurance│     │Banking  │          • Persistent state
└─────────┘     └─────────┘          • Plugin integration
```

### Why This Architecture?

**AzureAIAgent for Base Layer**
- Persistent state and conversation context
- Native plugin integration
- Deep Azure AI services integration
- Handles multi-step processes with memory

**ChatCompletionAgent for Routing**
- Fast routing decisions without state overhead
- Lightweight with minimal resource usage
- Plugin support for calling base agents
- Easy to modify routing logic

## Key Concepts

### Agent Specialization
- **Domain Experts**: Each base agent focuses on specific areas (insurance, banking, sales)
- **Plugin Integration**: Specialized tools and data sources for each domain
- **Context Retention**: Agents remember conversation history within their domain

### Intelligent Routing
- **Query Analysis**: Understanding user intent and domain requirements
- **Automatic Dispatch**: Routing queries to the most appropriate specialist
- **Multi-Domain Queries**: Coordinating multiple agents for complex requests

### Wrapper Plugin Pattern
Since AzureAIAgents cannot be used directly as plugins, we use wrapper patterns:

```python
class SpecialistWrapperPlugin:
    @kernel_function(description="Domain-specific functionality")
    async def specialist_function(self, query: str) -> str:
        response = await specialist_agent.get_response(messages=query)
        return response.content
```

## Next Steps

After mastering agent routing:
- [06-magentic-one-orchestration](../06-magentic-one-orchestration/) - Advanced orchestration patterns
- Build custom enterprise patterns for production-scale agent systems

🎉 **Ready to build intelligent agent hierarchies?** This tutorial will take you from basic routing concepts to production-ready agent orchestration systems that can handle complex, multi-domain queries with intelligent dispatch and coordination!
