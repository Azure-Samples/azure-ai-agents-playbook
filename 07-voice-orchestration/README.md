# 🎤 Voice Orchestration - Voice-Enabled Azure AI Agents

Welcome to the voice orchestration tutorials for Azure AI Agents! This folder contains comprehensive tutorials that demonstrate how to build sophisticated voice-controlled AI agents using Azure Speech Services and real-world API integrations.

## � What's In This Folder

### 🎤 [07.1 - Voice-Activated Currency Exchange Demo](07.1-voice-currency-exchange-demo.py)
**Complete voice-enabled currency exchange agent demo**

Learn to build production-ready voice agents with real API integration:
- 🎯 Real-time speech recognition with Azure Speech Services
- 🔧 Voice Activity Detection (VAD) for natural conversation flow
- 🤖 Currency exchange rates via Frankfurter API
- 💬 Voice-controlled financial data retrieval
- 🔄 WebSocket-based audio streaming for low latency
- 🧹 Production-ready voice processing patterns

**Perfect for**: Developers who want to build voice-controlled agents that can interact with external APIs and provide real-time financial data.

![Voice Agent](images/voice_agent.gif)

### 🔧 Core Components

#### **AgentVoice Class** (`voice.py`)
**Complete voice interaction framework**

The core voice processing framework that provides:
- ⚡ Real-time audio capture and processing
- 🎙️ Enterprise-grade speech-to-text conversion  
- 🔊 Voice Activity Detection for natural conversations
- 🌐 WebSocket streaming for minimal latency
- 🎛️ Audio enhancement and noise suppression
- 🔄 Async operations for responsive interactions

**Perfect for**: Understanding the technical foundations of voice-enabled AI agents and building your own voice interaction systems.

## 📁 Project Structure

```
07-voice-orchestration/
├── 07.1-voice-currency-exchange-demo.py    # Complete voice-enabled currency exchange agent demo
├── voice.py                                # Core voice processing framework
├── requirements.txt                        # Python dependencies
├── openapi_files/                          # API specifications
│   └── currency_exchange.json              # Frankfurter API OpenAPI spec
└── README.md                               # This file
```

## 🎯 Learning Path

We recommend exploring the voice orchestration components in this order:

1. **Start with the voice framework** - Understand the `voice.py` core components
2. **Run the currency exchange demo** - Experience voice-controlled API interactions
3. **Experiment with voice commands** - Test different natural language patterns
4. **Explore customization** - Adapt the framework for your own use cases

## 📋 Prerequisites

Before starting these tutorials, ensure you have:

### Azure Resources
- ✅ **Azure AI Foundry project** with deployed language model
- ✅ **Azure Speech Services resource** for voice recognition
- ✅ **Azure subscription** with appropriate permissions

### Required Knowledge
- ✅ Completed [01-agent-basics](../01-agent-basics/) tutorials
- ✅ Completed [02-agent-custom-functions](../02-agent-custom-functions/) tutorials  
- ✅ Understanding of OpenAPI tools from [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)
- ✅ Basic understanding of audio processing concepts

### System Requirements
- ✅ **Python 3.8+** installed
- ✅ **Working microphone and speakers/headphones**
- ✅ **Stable internet connection** for real-time audio streaming
- ✅ **Windows/macOS/Linux** with audio device support

### Environment Variables
Configure your Azure AI services by filling in the `.env` file at the project root level:

```bash
# Navigate to the project root and edit the .env file
cd ../../  # Go to azure-ai-agents-playbook root
# Edit .env file with your Azure AI configuration
```

The `.env` file should contain your Azure AI project details:
```properties
# Required for all voice tutorials
PROJECT_ENDPOINT="https://your-foundry-resource.services.ai.azure.com/api/projects/your-project-name"
MODEL_DEPLOYMENT_NAME="your-model-deployment-name"

# Required for Azure Speech Services
AZURE_VOICE_LIVE_API_KEY="your-speech-service-key"
AZURE_VOICE_LIVE_REGION="your-speech-region"
AZURE_VOICE_LIVE_ENDPOINT="https://your-cognitive-services.cognitiveservices.azure.com/"

# Optional: Additional Azure AI configuration
AZURE_OPENAI_API_KEY="your-azure-openai-api-key"
AZURE_OPENAI_ENDPOINT="https://your-openai-resource.openai.azure.com/"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
```

💡 **Tip**: The `.env` file is already present in the project root with example values. Simply update it with your Azure AI project details.

### Required Packages
The tutorial will install its required packages, but you can install them upfront:

```bash
# Navigate to the voice orchestration folder
cd azure-ai-agents-playbook/07-voice-orchestration

# Install required packages
pip install -r requirements.txt
```

## 🏃‍♂️ Running the Tutorial

### Voice-Enabled Currency Exchange Agent Demo

Run the complete voice-controlled currency exchange agent:

```bash
# Run the voice currency exchange demo
python 07.1-voice-currency-exchange-demo.py
```

**What this demo does:**
- Creates a voice-enabled agent that can get currency exchange rates
- Listens for voice commands through your microphone
- Processes natural language instructions about currency conversion
- Retrieves live exchange rates via Frankfurter API
- Provides voice feedback on currency data

**Example voice commands:**
- *"What is the current exchange rate from USD to EUR?"*
- *"Convert 100 dollars to Japanese yen"*
- *"Show me exchange rates for British pound"*
- *"What is 50 euros in Canadian dollars?"*
- *"Get the latest USD to GBP exchange rate"*

**Demo Flow:**
1. Agent starts listening for voice input
2. Speak your currency exchange command naturally
3. Agent processes speech and extracts currency details
4. Calls Frankfurter API to get live exchange rates
5. Provides voice feedback with current rates and conversions
6. Continues listening for additional commands



## � Key Concepts Covered

### 🎤 **Voice-Enabled AI Agents**
- Intelligent assistants powered by Azure AI with voice interaction
- Real-time speech recognition and natural language processing
- Voice Activity Detection for seamless conversations
- Integration with external APIs for real-world functionality

### 💱 **Currency Exchange Integration**
- **Frankfurter API**: Free foreign exchange rates API
- **OpenAPI Integration**: Structured API interaction patterns
- **Real-time Data**: Live currency conversion rates
- **Natural Language**: Voice commands for financial queries

### 🔧 **Development Approaches**

#### Voice Processing Framework
- Real-time audio capture and WebSocket streaming
- Azure Speech Services integration
- Voice Activity Detection algorithms
- Audio enhancement and noise suppression

#### API Integration Patterns
- OpenAPI specification handling
- Anonymous authentication for public APIs
- Error handling and retry logic
- Response formatting for voice feedback

### 🐍 **Production Patterns**
- Async/await for responsive voice interactions
- Context managers for resource management
- Exception handling for audio processing
- Type annotations for maintainable code

## 🏗️ What You'll Build

By the end of this tutorial, you'll have built:

1. **Voice-Controlled Agent** - AI assistant that responds to spoken commands
2. **Currency Exchange System** - Real-time financial data retrieval via voice
3. **Audio Processing Pipeline** - Production-ready voice input/output handling
4. **API Integration Pattern** - Reusable framework for voice-enabled API interactions

## � Additional Resources

- [Azure Speech Services Documentation](https://docs.microsoft.com/azure/cognitive-services/speech-service/)
- [Azure AI Agents Documentation](https://docs.microsoft.com/azure/ai-services/agents/)
- [Frankfurter API Documentation](https://www.frankfurter.app/docs/)
- [OpenAPI Specification Guide](https://swagger.io/specification/)

## 🎯 Next Steps

After completing this voice orchestration tutorial, explore:

- **[08-agent-routing](../08-agent-routing/)** - Intelligent agent selection and routing
- **[09-advanced-orchestrated-agents](../09-advanced-orchestrated-agents/)** - Complex multi-agent scenarios
- **Custom Voice Applications** - Build your own voice-enabled business solutions

---

🎤 **Ready to build voice-controlled financial AI agents?** Start with the currency exchange demo and explore the voice processing framework to create your own sophisticated voice-enabled applications!
