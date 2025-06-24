# Magentic-One Orchestration

🎪 **Master Advanced Multi-Agent Orchestration with Magentic-One Framework**

This folder explores the powerful Magentic-One orchestration framework for coordinating multiple Azure AI Agents in complex, multi-step workflows. Learn to create sophisticated agent systems that can handle creative tasks, research workflows, and intelligent information synthesis.

## 🎯 What You'll Learn

- **Magentic-One Framework**: Master the StandardMagenticManager for agent orchestration
- **Multi-Agent Coordination**: Build systems where agents collaborate intelligently
- **Complex Workflow Design**: Create pipelines that combine creativity, research, and analysis
- **Feedback Loop Implementation**: Design agents that learn from and improve each other's work
- **Research Automation**: Build agents that can conduct comprehensive web research
- **Creative Content Pipelines**: Develop systems for multi-step content creation

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Magentic-One Orchestrator                    │
│                  (StandardMagenticManager)                      │
└─────────────────────┬───────────────────────────────────────────┘
                      │
    ┌─────────────────┼─────────────────┬─────────────────┐
    │                 │                 │                 │
┌───▼────┐    ┌──────▼──────┐    ┌─────▼─────┐    ┌─────▼─────┐
│Creative│    │  Research   │    │   Fact    │    │  Report   │
│ Agent  │    │   Agent     │    │  Checker  │    │Generator  │
│        │    │             │    │           │    │           │
└───┬────┘    └──────┬──────┘    └─────┬─────┘    └─────┬─────┘
    │                │                 │                │
┌───▼────┐    ┌──────▼──────┐    ┌─────▼─────┐    ┌─────▼─────┐
│ Local  │    │ Bing Search │    │Cross-Ref  │    │  Output   │
│Plugin  │    │    Tool     │    │   Tool    │    │Formatter  │
└────────┘    └─────────────┘    └───────────┘    └───────────┘
```

![SK Orchestration](images/sk_orchestration.gif)


## 📁 Project Structure

```
06-magentic-one-orchestration/
├── 06.1-magentic_creative_writing_tutorial.ipynb    # Creative pipeline tutorial
├── 06.2-magentic_bing_search_orchestration_tutorial.ipynb # Research workflow tutorial
└── README.md                                        # This file
```

## 📚 Tutorials

### 06.1 - Magentic Creative Writing Pipeline
**🎨 Multi-Agent Creative Content System**

Learn to orchestrate a creative workflow where multiple agents collaborate:
- **Joke Writer Agent**: Creates original jokes based on topics
- **Haiku Converter Agent**: Transforms jokes into haiku format
- **French Translator Agent**: Translates content to French
- **Local Plugins**: Topic classification and quality feedback

**Key Features:**
- Creative content pipeline automation
- Feedback loops between agents
- Local plugin integration
- Quality assessment and iteration

### 06.2 - Magentic Bing Search Research Pipeline
**🔍 Intelligent Web Research Orchestration**

Build sophisticated research agents that can:
- **Research Agent**: Conduct targeted web searches using Bing
- **Fact Checker Agent**: Verify information across multiple sources
- **Report Generator Agent**: Synthesize findings into comprehensive reports
- **Complex Query Decomposition**: Break down multi-part questions

**Key Features:**
- Multi-step research workflows
- Information verification and cross-referencing
- Intelligent query decomposition
- Comprehensive report generation

## 🛠️ Prerequisites

### Required Azure Resources
- **Azure AI Project** with deployed language model (GPT-4 recommended)
- **Azure AI Foundry Project** (for Bing Search tutorial)
- **Bing Search Connection** configured in Azure AI Studio (for tutorial 06.2)

### Environment Variables
Configure your environment with the following variables in the `.env` file at the project root:

```bash
# Azure AI Configuration (Required for both tutorials)
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="gpt-4o"  # or your deployed model

# Additional for tutorial 06.2 (Bing Search Research)
AZURE_FOUNDRY_PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"

# Note: Bing Search connection should be configured in Azure AI Studio
# The tutorial will automatically discover available Bing Search connections
```

### Configuration Steps of the Grounding with Bing Search Connection

Please follow the below two links to properly configure the Grounding with Bing Search Connection in Azure AI Studio:

- [Create a Grounding with Bing Search Connection](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding)
- [Create a Grounding with Bing Search Connection in Azure AI Studio](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-code-samples?pivots=portal)


### Required Python Packages
```bash
pip install azure-ai-agents
pip install azure-identity
pip install semantic-kernel
pip install azure-ai-projects  # For Bing Search tutorial
pip install python-dotenv
```

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Clone the repository
git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
cd azure-ai-agents-playbook/06-magentic-one-orchestration

# Set up environment variables (create .env file at project root)
# Add all required environment variables listed above
```

### 2. Run Creative Pipeline Tutorial
```bash
# Start Jupyter Notebook
jupyter notebook 06.1-magentic_creative_writing_tutorial.ipynb

# Follow the notebook to create a multi-agent creative system
```

### 3. Run Research Pipeline Tutorial
```bash
# Ensure Bing Search connection is configured in Azure AI Studio
# The tutorial will automatically discover available connections
jupyter notebook 06.2-magentic_bing_search_orchestration_tutorial.ipynb
```

## 💡 Tutorial Highlights

### Creative Pipeline (06.1) Features:
- **Simple Architecture**: No external API dependencies
- **Local Plugins**: Topic selection and haiku classification
- **Feedback Loops**: Length-based content adjustment
- **File Operations**: Temporary file storage for haiku analysis
- **Random Topic Selection**: From predefined topic list

### Research Pipeline (06.2) Features:
- **Bing Search Integration**: Automatic connection discovery
- **Complex Query Decomposition**: Multi-step research process
- **Fact Verification**: Cross-referencing multiple sources
- **Comprehensive Reporting**: Structured research reports
- **Real-world Use Case**: "43rd president chief of staff education" research

## 🧩 Learning Path

### Beginner Level
1. **Understanding Magentic-One**: Learn the orchestration framework basics
2. **Simple Agent Coordination**: Start with 2-3 agents working together
3. **Local Plugin Integration**: Add custom tools to your agents

### Intermediate Level
1. **Creative Workflows**: Build content generation pipelines
2. **Feedback Mechanisms**: Implement agent-to-agent learning
3. **Quality Assessment**: Add evaluation and improvement loops

### Advanced Level
1. **Complex Research Systems**: Multi-step information gathering
2. **Dynamic Orchestration**: Adaptive workflow management
3. **Cross-Domain Integration**: Combine creative and analytical tasks

## 💡 Key Concepts

### Magentic-One Framework
- **StandardMagenticManager**: Core orchestration engine
- **Agent Coordination**: Intelligent task distribution
- **Pipeline Management**: Sequential and parallel execution
- **State Management**: Maintaining context across agent interactions

### Agent Specialization
- **Role-Based Design**: Each agent has specific expertise
- **Tool Integration**: Agents use specialized tools and plugins
- **Communication Protocols**: Structured inter-agent messaging
- **Quality Control**: Built-in evaluation and feedback mechanisms

### Workflow Patterns
- **Sequential Processing**: Step-by-step task completion
- **Parallel Execution**: Concurrent agent operations
- **Feedback Loops**: Iterative improvement cycles
- **Dynamic Routing**: Adaptive task assignment

## 🔧 Advanced Configuration

### Custom Agent Types
```python
# Create specialized agents with custom tools
creative_agent = Agent(
    name="CreativeWriter",
    instructions="Create engaging, original content",
    tools=[topic_classifier, creativity_enhancer]
)

research_agent = Agent(
    name="WebResearcher", 
    instructions="Find and verify information online",
    tools=[bing_search, fact_checker, source_validator]
)
```

### Orchestration Patterns
```python
# Configure complex workflows
manager = StandardMagenticManager(
    agents=[creative_agent, research_agent, synthesizer_agent],
    coordination_strategy="intelligent_routing",
    feedback_enabled=True,
    quality_threshold=0.8
)
```

## 🐛 Troubleshooting

### Common Issues

**Magentic-One Import Errors**
```bash
# Install latest Semantic Kernel
pip install --upgrade semantic-kernel

# Verify Magentic-One availability
python -c "from semantic_kernel.agents.open_ai import MagenticOneGroupChat; print('Available')"
```

**Agent Coordination Failures**
```bash
# Check agent configuration
print(f"Agents configured: {len(manager.agents)}")
print(f"Communication channels: {manager.communication_status}")

# Verify model deployments
az cognitiveservices account deployment list --name <openai-resource>
```

**Performance Optimization**
```bash
# Monitor agent performance
manager.enable_telemetry(True)
manager.set_timeout(300)  # 5 minutes

# Optimize for parallel execution
manager.enable_parallel_processing(True)
```

### Error Resolution

**Tool Integration Issues**
- Verify all required API keys are configured
- Check tool function signatures match expected format
- Ensure proper error handling in custom plugins

**Memory and State Management**
- Monitor conversation history size
- Implement state cleanup between runs
- Use conversation summarization for long workflows

##  Advanced Patterns

### Dynamic Orchestration
```python
# Adaptive workflow management
class DynamicOrchestrator:
    def route_task(self, task_complexity, available_agents):
        if task_complexity > 0.8:
            return self.parallel_execution(available_agents)
        else:
            return self.sequential_execution(available_agents)
```

### Quality Assessment
```python
# Multi-layered quality control
class QualityController:
    def evaluate_output(self, content, criteria):
        scores = []
        for criterion in criteria:
            score = self.assess_criterion(content, criterion)
            scores.append(score)
        return sum(scores) / len(scores)
```

### Cross-Domain Integration
```python
# Combine creative and analytical capabilities
class HybridPipeline:
    def __init__(self):
        self.creative_agents = [joke_writer, poet, storyteller]
        self.analytical_agents = [fact_checker, data_analyst, reviewer]
        self.synthesizer = content_synthesizer
```

## 📚 Additional Resources

### Documentation
- [Semantic Kernel Agents](https://learn.microsoft.com/semantic-kernel/agents/)
- [Azure OpenAI Service](https://docs.microsoft.com/azure/cognitive-services/openai/)
- [Magentic-One Framework](https://github.com/microsoft/semantic-kernel)
- [Bing Search API](https://docs.microsoft.com/bing/search-apis/)

### Community & Support
- [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [Azure AI Community](https://techcommunity.microsoft.com/t5/azure-ai/ct-p/AzureAI)
- [Stack Overflow - Semantic Kernel](https://stackoverflow.com/questions/tagged/semantic-kernel)

## 🚀 Next Steps

After mastering Magentic-One orchestration, explore:

1. **Multi-Modal Agents**: Integrate vision and voice capabilities
2. **Enterprise Integration**: Connect to business systems and databases
3. **Custom Orchestration**: Build your own orchestration frameworks
4. **Production Deployment**: Scale agent systems in cloud environments
5. **Advanced AI Patterns**: Explore emerging multi-agent architectures

---

**Ready to orchestrate intelligent agent workflows?** 🎪✨
