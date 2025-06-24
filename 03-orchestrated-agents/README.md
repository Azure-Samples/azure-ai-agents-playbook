# 🎭 Orchestrated Agents - Multi-Agent Coordination

Welcome to the world of multi-agent orchestration! This folder contains comprehensive tutorials that show you how to coordinate multiple Azure AI agents working together to solve complex problems through sophisticated collaboration patterns.

## 📚 What's In This Folder

### 🔄 [03.1 - Concurrent and Sequential Orchestration Tutorial](03.1-concurrent_and_sequential_orchestration_tutorial.ipynb)
**Master the art of multi-agent orchestration with Semantic Kernel**

Learn advanced coordination patterns with specialized agent teams:
- 🎯 Understanding orchestration patterns and when to use them
- 🔄 Sequential orchestration for pipeline workflows (Agent A → Agent B → Agent C)
- ⚡ Concurrent orchestration for parallel processing (A + B + C → Combine)
- 🏗️ Creating specialized agents with domain-specific plugins
- 📊 Performance comparison between orchestration patterns
- 🛠️ Advanced Semantic Kernel orchestration features

**Perfect for**: Developers who want to build sophisticated multi-agent systems that can handle complex workflows through coordinated agent collaboration.


#### Orchestration Patterns
- **Sequential Orchestration**: Agents work in a pipeline, passing results from one to the next.
![Sequential Orchestration](images/sequential_orchestration.gif)

- **Concurrent Orchestration**: Agents work in parallel, combining results at the end.
![Concurrent Orchestration](images/concurrent_orchestration.gif)



### 🤝 [03.2 - Connected Agents Tutorial](03.2-connected_agents_tutorial.ipynb)
**Learn agent-to-agent communication and hybrid orchestration approaches**

Explore different approaches to agent connectivity and collaboration:
- 🔗 Azure AI Foundry SDK connected agents using ConnectedAgentTool
- 🔌 Semantic Kernel AzureAIAgent plugins for hybrid workflows
- 🎯 Agent specialization and task delegation patterns
- 🔄 Comparison between direct connection vs plugin wrapping
- 🚀 Hybrid workflows combining both SDK approaches
- 💡 Best practices for agent communication architectures

**Perfect for**: Developers who want to understand different agent connection patterns and build systems that leverage both Azure AI Foundry and Semantic Kernel capabilities.

![Connected Agents](images/connected_agents.gif)


## 🎯 Learning Path

We recommend following the tutorials in this order:

1. **Start with 03.1** - Master orchestration patterns with specialized agent teams
2. **Advance to 03.2** - Learn agent connectivity and hybrid approaches

**Prerequisites**: Complete the [01-agent-basics](../01-agent-basics/) and [02-agent-custom-functions](../02-agent-custom-functions/) tutorials first to understand core concepts and function integration.

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Previous Knowledge
- ✅ Completed [01-agent-basics](../01-agent-basics/) tutorials
- ✅ Completed [02-agent-custom-functions](../02-agent-custom-functions/) tutorials
- ✅ Understanding of Azure AI Agents and custom functions/plugins
- ✅ Basic knowledge of async/await patterns in Python

### Azure Resources
- ✅ Azure subscription
- ✅ Azure AI Foundry project
- ✅ Deployed AI model (GPT-4, GPT-3.5-turbo, etc.)
- ✅ Azure OpenAI resource (for Semantic Kernel scenarios)

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

# Required for Semantic Kernel orchestration (03.1)
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
pip install azure-ai-agents azure-identity semantic-kernel python-dotenv
```

## 🔑 Key Concepts Covered

### 🎭 **Multi-Agent Orchestration**

**What orchestration enables:**
- 🎯 **Specialization**: Each agent excels in specific domains
- ⚡ **Parallel Processing**: Multiple agents work simultaneously  
- 📈 **Better Results**: Domain experts produce higher quality outputs
- 🔄 **Scalability**: Add more agents as needed
- 💪 **Resilience**: If one agent fails, others continue

### 🔄 **Orchestration Patterns**

#### Sequential Orchestration (Pipeline)
- **Flow**: Agent A → Agent B → Agent C
- **Use Cases**: Document processing, analysis workflows, step-by-step procedures
- **Benefits**: Quality control, context building, dependent task chains
- **Example**: Research Agent → Analytics Agent → Content Agent

#### Concurrent Orchestration (Parallel)
- **Flow**: Agent A + Agent B + Agent C → Combine Results
- **Use Cases**: Independent tasks, multi-source research, parallel processing
- **Benefits**: Speed, efficiency, diverse perspectives
- **Example**: Multiple research agents gathering different data sources

#### Hybrid Patterns
- **Flow**: Mix of sequential and concurrent patterns
- **Use Cases**: Complex workflows with both dependent and independent tasks
- **Benefits**: Optimal performance and quality for complex scenarios

### 🤝 **Agent Connectivity Approaches**

#### Connected Agents (Foundry SDK)
- **Method**: `ConnectedAgentTool` for agent-to-agent communication
- **Pattern**: Agent calls other agents as tools
- **Benefits**: Direct delegation, simple coordination, built-in tool management
- **Use Cases**: Task delegation, specialized function calls

#### AzureAI Plugins (Semantic Kernel)
- **Method**: Wrap Azure AI agents as Semantic Kernel plugins
- **Pattern**: Hybrid SK orchestration with Azure AI power
- **Benefits**: Rich orchestration features, type safety, advanced patterns
- **Use Cases**: Complex workflows, enterprise scenarios, hybrid architectures

### 🏗️ **Advanced Architecture Patterns**

- **Agent Specialization**: Creating domain-expert agents
- **Plugin Libraries**: Reusable agent capabilities
- **Workflow Optimization**: Performance tuning and pattern selection
- **Error Handling**: Resilient multi-agent systems
- **Resource Management**: Efficient agent lifecycle management

## 🏗️ What You'll Build

By the end of these tutorials, you'll have built:

### 🎭 **Sophisticated Agent Teams**
1. **Research + Analytics + Content Pipeline** - Sequential workflow for comprehensive analysis
2. **Multi-Perspective Analysis System** - Concurrent agents providing diverse insights
3. **Specialized Agent Network** - Domain experts working together
4. **Hybrid Orchestration Systems** - Combining multiple patterns for optimal results

### 🔄 **Advanced Orchestration Patterns**
1. **Pipeline Workflows** - Step-by-step agent processing chains
2. **Parallel Processing** - Simultaneous multi-agent execution
3. **Dynamic Coordination** - Adaptive workflow routing
4. **Error-Resilient Systems** - Graceful failure handling and recovery

### 🤝 **Agent Communication Systems**
1. **Tool-Based Delegation** - Agents calling other agents as tools
2. **Plugin Integration** - Wrapping agents as reusable plugins
3. **Hybrid Architectures** - Combining Foundry SDK and Semantic Kernel
4. **Enterprise Patterns** - Production-ready agent coordination

##  Additional Resources

- [Semantic Kernel Orchestration Documentation](https://learn.microsoft.com/semantic-kernel/agents/)
- [Azure AI Agents Connected Tools Documentation](https://docs.microsoft.com/azure/ai-services/agents/tools/)
- [Multi-Agent Systems Design Patterns](https://docs.microsoft.com/azure/ai-services/patterns/)
- [Azure AI Foundry Orchestration Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/)

## 🎯 Next Steps

After mastering orchestrated agents, explore:

- **[04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)** - Adding external tools and APIs to orchestrated workflows
- **[05-orchestrated-agents-with-custom-openapi-tools](../05-orchestrated-agents-with-custom-openapi-tools/)** - Building custom API integrations for agent teams
- **[06-magentic-one-orchestration](../06-magentic-one-orchestration/)** - Advanced multi-agent orchestration patterns

---

🎉 **Ready to orchestrate sophisticated agent teams?** Start with sequential orchestration patterns and progress to advanced concurrent and hybrid workflows to build truly intelligent multi-agent systems!
