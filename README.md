# Azure AI Agents Orchestration Playbook

A comprehensive collection of tutorials for building production-ready Azure AI Agents, from basic conversations to complex multi-agent orchestration systems with voice capabilities and external API integrations.

> **Note:** Check out our **animated** PowerPoint presentation for an overview: [Azure AI Agents Orchestration Playbook Presentation](./Azure%20AI%20Agent%20Orchestration.pptx)

## Tutorial Structure

### Foundational Concepts
- **[01-agent-basics](01-agent-basics/)** - Core Azure AI Agents fundamentals using Foundry SDK and Semantic Kernel
- **[02-agent-custom-functions](02-agent-custom-functions/)** - Extend agent capabilities with custom functions and plugins

### Multi-Agent Systems
- **[03-orchestrated-agents](03-orchestrated-agents/)** - Coordinate multiple agents for complex workflows
- **[04-orchestrated-agents-with-tools](04-orchestrated-agents-with-tools/)** - Integrate external APIs and Azure Logic Apps
- **[05-orchestrated-agents-with-custom-openapi-tools](05-orchestrated-agents-with-custom-openapi-tools/)** - Connect agents to custom FastAPI services
- **[06-magentic-one-orchestration](06-magentic-one-orchestration/)** - Advanced orchestration with Magentic-One framework

### Advanced Capabilities
- **[07-voice-orchestration](07-voice-orchestration/)** - Voice-enabled agents with real-time audio processing
- **[08-agent-routing](08-agent-routing/)** - Hierarchical routing design pattern for multi-agent systems


![Agent Router](08-agent-routing/images/router.gif)



## Getting Started

### Prerequisites
- Azure subscription with AI services
- Azure AI Foundry project with deployed models
- Python 3.8+ with Jupyter support

### Quick Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Azure-Samples/azure-ai-agents-playbook.git
   cd azure-ai-agents-playbook
   ```

2. **Configure environment**
   - Update `.env` file with your Azure AI project details
   - Install dependencies: `pip install -r requirements.txt`

3. **Start learning**
   - Begin with [01-agent-basics](01-agent-basics/) for fundamentals
   - Progress through tutorials in numerical order

## Learning Path

**Recommended progression:**

1. **Basics** → Learn core Azure AI Agents concepts and development patterns
2. **Functions** → Add custom capabilities to extend agent functionality  
3. **Orchestration** → Coordinate multiple agents for complex workflows
4. **Tools** → Integrate external services and automation workflows
5. **Custom APIs** → Connect agents to your own business services
6. **Advanced** → Master sophisticated orchestration frameworks
7. **Voice** → Add voice interaction capabilities

## What You'll Build

By completing this playbook, you'll master:

- **Conversational AI Agents** with persistent context and memory
- **Multi-Agent Systems** that collaborate intelligently
- **Tool-Enhanced Agents** connected to external APIs and services  
- **Voice-Enabled Agents** with real-time audio processing
- **Enterprise Workflows** combining AI with business automation
- **Production Patterns** for scalable and reliable agent systems

## 🔧 Key Technologies

- **Azure AI Agents** - Core agent development platform
- **Azure AI Foundry SDK** - Official Microsoft agent framework
- **Semantic Kernel** - Advanced orchestration and plugin system
- **Azure Speech Services** - Voice recognition and synthesis
- **Azure Logic Apps** - Workflow automation and integration
- **FastAPI** - Custom API development and OpenAPI integration

## 📋 Environment Configuration

Each tutorial folder contains specific setup instructions. The main environment variables needed:

- `PROJECT_ENDPOINT` - Your Azure AI Foundry project endpoint
- `MODEL_DEPLOYMENT_NAME` - Your deployed AI model name
- `AZURE_OPENAI_*` - Azure OpenAI configuration for Semantic Kernel
- `AZURE_VOICE_*` - Speech services for voice tutorials

## 🎪 Tutorial Highlights

**Real-world scenarios you'll implement:**
- Financial assistants analyzing bank transactions
- Research agents conducting web searches and fact-checking
- Creative content pipelines with multi-agent collaboration
- Email automation through voice commands
- Currency exchange agents with live API data
- Complex business workflows with AI decision-making

## 🔗 Additional Resources

- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)

---

**Ready to build the future of AI agents?** 🚀🤖
