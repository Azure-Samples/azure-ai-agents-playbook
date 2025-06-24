# Voice Orchestration

Learn how to build voice-enabled Azure AI Agents that can listen, process speech, and respond with real-world data. Create agents that interact naturally through voice commands and integrate with external APIs.

## What's In This Folder

**[07.1 - Voice-Activated Currency Exchange Demo](07.1-voice-currency-exchange-demo.py)**
Complete voice-enabled currency exchange agent that uses Azure Speech Services for real-time voice interaction with the Frankfurter API for live exchange rates.

![Voice Agent](images/voice_agent.gif)

**[AgentVoice Class](voice.py)**
Core voice processing framework that provides real-time audio capture, speech-to-text conversion, voice activity detection, and WebSocket streaming for minimal latency.

## Project Structure

```
07-voice-orchestration/
├── 07.1-voice-currency-exchange-demo.py    # Complete voice demo
├── voice.py                                # Core voice framework
├── requirements.txt                        # Python dependencies
├── openapi_files/                          # API specifications
│   └── currency_exchange.json              # Frankfurter API spec
└── README.md                               # This file
```

## Learning Path

1. **Understand the voice framework** - Explore the `voice.py` core components
2. **Run the currency exchange demo** - Experience voice-controlled API interactions  
3. **Experiment with voice commands** - Test different natural language patterns

## Prerequisites

### Azure Resources
- Azure AI Foundry project with deployed language model
- Azure Speech Services resource for voice recognition
- Azure subscription with appropriate permissions

### Previous Knowledge
- Complete [01-agent-basics](../01-agent-basics/) tutorials
- Complete [02-agent-custom-functions](../02-agent-custom-functions/) tutorials  
- Understanding of OpenAPI tools from [04-orchestrated-agents-with-tools](../04-orchestrated-agents-with-tools/)

### System Requirements
- Python 3.8+
- Working microphone and speakers/headphones
- Stable internet connection for real-time audio streaming
- Windows/macOS/Linux with audio device support

### Environment Variables
Configure your Azure AI services in the `.env` file at the project root:

```bash
# Navigate to the project root and edit the .env file
cd ../../  # Go to azure-ai-agents-playbook root
```

Update the `.env` file with your Azure AI project details:
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

**Tip**: The `.env` file already exists in the project root with example values - just update it with your details.

### Required Packages
Install the packages you need:

```bash
# Navigate to the voice orchestration folder
cd azure-ai-agents-playbook/07-voice-orchestration

# Install required packages
pip install -r requirements.txt
```

## Running the Tutorial

### Voice-Enabled Currency Exchange Demo

```bash
# Run the voice currency exchange demo
python 07.1-voice-currency-exchange-demo.py
```

**What this demo does:**
- Creates a voice-enabled agent that gets currency exchange rates
- Listens for voice commands through your microphone
- Processes natural language instructions about currency conversion
- Retrieves live exchange rates via Frankfurter API
- Provides voice feedback on currency data

**Example voice commands:**
- "What is the current exchange rate from USD to EUR?"
- "Convert 100 dollars to Japanese yen"
- "Show me exchange rates for British pound"
- "What is 50 euros in Canadian dollars?"
- "Get the latest USD to GBP exchange rate"

**Demo Flow:**
1. Agent starts listening for voice input
2. Speak your currency exchange command naturally
3. Agent processes speech and extracts currency details
4. Calls Frankfurter API to get live exchange rates
5. Provides voice feedback with current rates and conversions
6. Continues listening for additional commands

## What You'll Learn

### Voice-Enabled AI Agents
- Intelligent assistants with voice interaction capabilities
- Real-time speech recognition and natural language processing
- Voice Activity Detection for seamless conversations
- Integration with external APIs for real-world functionality

### Currency Exchange Integration
- **Frankfurter API**: Free foreign exchange rates API
- **OpenAPI Integration**: Structured API interaction patterns
- **Real-time Data**: Live currency conversion rates
- **Natural Language**: Voice commands for financial queries

### Voice Processing Framework
- Real-time audio capture and WebSocket streaming
- Azure Speech Services integration
- Voice Activity Detection algorithms
- Audio enhancement and noise suppression

### Production Patterns
- Async/await for responsive voice interactions
- Context managers for resource management
- Exception handling for audio processing
- Type annotations for maintainable code

## What You'll Build

By the end of this tutorial, you'll have built:
- **Voice-Controlled Agent** - AI assistant that responds to spoken commands
- **Real-Time Audio Processing** - System that captures and processes voice input
- **API Integration** - Voice-driven external service interaction
- **Natural Conversation Flow** - Seamless voice interaction patterns

## Next Steps

After mastering voice orchestration:
- [08-agent-routing](../08-agent-routing/) - Hierarchical agent routing patterns
- Explore multi-modal interactions combining voice with other input methods
