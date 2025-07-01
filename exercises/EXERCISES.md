# Azure AI Agents Workshop Exercises

This document contains practical exercises for learning Azure AI Agents development. Each exercise builds upon the concepts from the playbook tutorials and provides hands-on experience with real-world scenarios.

## Prerequisites

Before starting these exercises, ensure you have:
- Completed the basic tutorials in [01-agent-basics](01-agent-basics/)
- Azure AI Foundry project configured
- Python environment set up with required packages
- `.env` file configured with your Azure credentials

## Beginner Level Exercises

### Exercise 1: Personal Assistant Agent
**Difficulty**: Beginner  
**Time**: 15-20 minutes  
**Skills**: Basic agent creation, custom functions

**Scenario**: Create a personal assistant agent that helps with daily tasks like scheduling, weather checks, and simple calculations.

**Requirements**:
1. Create an agent with a friendly personality
2. Add custom functions for:
   - Current date/time information
   - Simple calculator (add, subtract, multiply, divide)
   - Random motivational quote generator
3. Test the agent with conversational queries like:
   - "What time is it?"
   - "Calculate 25 * 4"
   - "Give me a motivational quote"

**Files to create**:
- `exercises/personal_assistant.py`
- Include error handling and type hints

**Learning outcomes**:
- Basic agent configuration
- Function registration
- Conversational interaction patterns

---

### Exercise 2: Voice-Enabled Stock Market Agent
**Difficulty**: Medium  
**Time**: 20-30 minutes  
**Skills**: Voice interaction, API integration, financial data processing

**Scenario**: Build a voice-controlled agent that provides real-time stock market information and analysis.

**Requirements**:
1. Get free Vatnage API Key from [here](https://www.alphavantage.co/support/#api-key)
2. Add `voice.py` python [file](../07-voice-orchestration/voice.py) from the 07 tutorial to the same folder you're working in
3. Use the already provided Alpha Vantage [OpenAPI JSON](openapi_files/stock_market.json) file to register the tool
4. Create an agent specialized in stock market data using the usual way, and then create an `AgentVoice` class instance
5. Test with voice-style prompts like:
    - "What's the current price of Apple stock?"
    - "Show me Microsoft's stock performance this week"
    - "Compare Tesla and Ford stock prices"

**Files to create**:
- `exercises/voice_stock_agent.py`

**Learning outcomes**:
- Voice command processing
- Real-time API data integration
- Financial data analysis patterns

---


## Getting Started

1. Create an `exercises/` directory in your workspace
2. Copy the basic setup from the playbook tutorials
3. Refer back to the main playbook tutorials for detailed examples


## Resources

- [Azure AI Agents Documentation](https://learn.microsoft.com/en-us/azure/ai-services/agents/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/en-us/semantic-kernel/)
- [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry/)
- [Main Playbook Tutorials](README.md)

Happy coding! 🚀
