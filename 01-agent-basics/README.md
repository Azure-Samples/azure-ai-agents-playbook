# 🤖 Agent Basics - Azure AI Agents Fundamentals

Welcome to the foundational tutorials for Azure AI Agents! This folder contains comprehensive tutorials that cover the fundamentals of creating and managing AI agents using different approaches and frameworks.

## 📚 What's In This Folder

### 🔧 [01.1 - Azure AI Agents Foundry SDK Tutorial](01.1-azure_ai_agents_foundry_sdk_tutorial.ipynb)
**Complete beginner's guide to Azure AI Agents using the Foundry SDK**

Learn the fundamentals with the official Azure AI Agents SDK:
- 🎯 Understanding what Azure AI Agents are
- 🔧 Setting up your development environment
- 🤖 Creating your first agent
- 💬 Managing conversations with threads
- 🔄 Multi-turn conversations with context retention
- 🧹 Proper resource management and cleanup

**Perfect for**: Developers new to Azure AI Agents who want to understand the core concepts using Microsoft's official SDK.


![Single Agent](images/single_agent.gif)


### 🧠 [01.2 - Azure AI Agents with Semantic Kernel Tutorial](01.2-azure_ai_agents_semantic_kernel_tutorial.ipynb)
**Advanced agent development using Semantic Kernel orchestration**

Explore the power of Semantic Kernel with Azure AI Agents:
- 🚀 Enhanced agent capabilities with Semantic Kernel
- 🔌 Plugin system for extending agent functionality
- ⚡ Async operations and streaming responses
- 🎯 Custom function calling and tool integration
- 🔄 Advanced conversation patterns
- 🏗️ Building reusable agent components

**Perfect for**: Developers who want to leverage Semantic Kernel's orchestration capabilities for more sophisticated agent scenarios.

![Single Agent with SK Wrapper](images/single_agent_with_sk.gif)


### 🐍 [01.3 - Python `with` Statement Tutorial](01.3-python_with_statement_agents_tutorial.ipynb)
**Understanding context management and best practices**

Master proper resource management with Python context managers:
- 🧠 Understanding the Python `with` statement
- ✅ When to use `with` vs manual resource management
- 🔧 Foundry SDK context management patterns
- 🔄 Semantic Kernel async context management
- 💡 Best practices for production applications
- 🚫 Common pitfalls and how to avoid them

**Perfect for**: Developers who want to write cleaner, more reliable code with proper resource management.

## 🎯 Learning Path

We recommend following the tutorials in this order:

1. **Start with 01.1** - Get familiar with the core Azure AI Agents concepts
2. **Explore 01.2** - Understand the enhanced capabilities with Semantic Kernel
3. **Master 01.3** - Learn proper resource management patterns

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Azure Resources
- ✅ Azure subscription
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)

### Environment Setup
- ✅ Python 3.8+ installed
- ✅ Jupyter Notebook or VS Code with notebook support
- ✅ Azure CLI (optional, for authentication)

### Environment Variables
Configure your Azure AI services by filling in the `.env` file at the project root level:

```bash
# Navigate to the project root and edit the .env file
cd ../../  # Go to azure-ai-agents-playbook root
# Edit .env file with your Azure AI configuration
```

The `.env` file should contain your Azure AI project details:
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
REASONING_MODEL_DEPLOYMENT_NAME="your-reasoning-model"
AZURE_SUBSCRIPTION_ID="your-subscription-id"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
Each tutorial will install its required packages, but you can install them all upfront:

```bash
pip install azure-ai-agents azure-identity semantic-kernel
```

## 🔑 Key Concepts Covered

### 🤖 **Azure AI Agents**
- Intelligent assistants powered by Azure AI
- Persistent conversation memory through threads
- Ability to use tools and perform tasks
- Scalable and enterprise-ready

### 💬 **Conversation Management**
- **Threads**: Conversation sessions that maintain context
- **Messages**: Individual interactions within a thread
- **Runs**: The agent's processing and response generation
- **Context Retention**: Maintaining conversation history

### 🔧 **Development Approaches**

#### Foundry SDK Approach
- Direct integration with Azure AI services
- Simple, straightforward API patterns
- Built-in authentication and error handling
- Perfect for getting started quickly

#### Semantic Kernel Approach  
- Enhanced orchestration capabilities
- Rich plugin ecosystem
- Advanced async patterns
- Type-safe development experience
- Enterprise-grade features

### 🐍 **Python Best Practices**
- Context managers (`with` statement)
- Async/await patterns
- Resource management
- Exception handling
- Type annotations

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

1. **Basic Agents** - Simple conversational AI assistants
2. **Context-Aware Agents** - Agents that remember conversation history
3. **Plugin-Enhanced Agents** - Agents with custom capabilities (math, weather, etc.)
4. **Production-Ready Patterns** - Proper resource management and error handling

## 📖 Additional Resources

- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Python Context Managers Guide](https://docs.python.org/3/library/contextlib.html)

## 🎯 Next Steps

After completing these fundamental tutorials, explore:

- **[02-agent-custom-functions](../02-agent-custom-functions/)** - Adding custom capabilities to your agents
- **[03-orchestrated-agents](../03-orchestrated-agents/)** - Coordinating multiple agents
- **[04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)** - Integrating external tools and APIs

---

🎉 **Ready to become an Azure AI Agents expert?** Start with the first tutorial and work your way through all three to master the fundamentals!
