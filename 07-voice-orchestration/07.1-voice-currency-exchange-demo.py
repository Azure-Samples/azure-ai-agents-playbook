# Voice-Activated Currency Exchange Agent Demo
# Voice-controlled agent that can get currency exchange rates via API

# Import necessary libraries and load environment variables
import os
import asyncio
import json
import requests
from datetime import datetime
from typing import Annotated, Dict, Any, Callable, Set
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv(override=True)

# Import Azure AI Foundry SDK
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import ToolSet, FunctionTool
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import OpenApiTool, OpenApiAnonymousAuthDetails

# Import our voice module
from voice import AgentVoice

print("📦 All packages imported successfully!")
print("🔧 Ready to create voice-enabled currency exchange agent!")

# Verify environment variables
required_vars = ['PROJECT_ENDPOINT', 'MODEL_DEPLOYMENT_NAME']

for var in required_vars:
    if var in os.environ:
        print(f"✅ {var} is set")
    else:
        print(f"❌ {var} is missing!")


print("✅ Currency exchange tool ready!")

# Step 2: Create a voice-controlled currency exchange agent
async def create_currency_agent():
    """Create an Azure AI agent with currency exchange capabilities."""

    # Get required environment variables
    model_deployment_name = os.environ.get("MODEL_DEPLOYMENT_NAME")
    endpoint = os.environ.get("PROJECT_ENDPOINT")


    if not model_deployment_name or not endpoint:
        raise ValueError("Missing required environment variables: MODEL_DEPLOYMENT_NAME and PROJECT_ENDPOINT")

    # Create the currency exchange tool instance
    credential = DefaultAzureCredential()
    agents_client = AgentsClient(endpoint=endpoint, credential=credential)

    # Load the currency exchange OpenAPI specification
    currency_spec_path = os.path.join("openapi_files", "currency_exchange.json")

    with open(currency_spec_path, "r") as f:
        currency_openapi_spec = json.loads(f.read())

    # Create OpenAPI tool for currency exchange
    auth = OpenApiAnonymousAuthDetails()

    currency_tool = OpenApiTool(
        name="currency_exchange",
        spec=currency_openapi_spec,
        description="Get the latest foreign exchange rates from Frankfurter API",
        auth=auth
    )

    print("💱 Currency exchange OpenAPI tool created")
    print(f"Available operations: {len(currency_tool.definitions)}")


    # Create agent with proper toolset
    with agents_client:        # Create the agent with the currency exchange tool
        print("🤖 Creating currency exchange agent with API capabilities...")
        
        agent = agents_client.create_agent(
            model=model_deployment_name,
            name="currency_exchange_agent",
            instructions="You are a helpful currency exchange agent. Use the currency exchange API to get latest exchange rates. Always provide clear explanations of the rates. Your responses are SUPER concise.",            tools=currency_tool.definitions
        )  
        
        print(f"🤖 Created currency exchange agent: {agent.name}")
        print(f"🔧 Agent has currency exchange capabilities")
        print(f"🆔 Agent ID: {agent.id}")
    
    return agent, agents_client

async def main():
    """Main function to run the voice-activated currency exchange assistant demo."""
    
    print("🎙️ Starting Voice-Activated Currency Exchange Assistant Demo")
    print("=" * 60)
    
    try:
        # Create the currency exchange agent
        print("Creating currency exchange agent with API integration...")
        agent, agents_client = await create_currency_agent()
          # Create voice interface with the agent  
        print("\n🎤 Setting up voice interface...")
        av = AgentVoice(agent_id=agent.id)
        
        print("\n🗣️ Voice interface ready!")
        print("Sample voice commands you can try:")
        print("• 'What is the current exchange rate from USD to EUR?'")
        print("• 'Convert 100 dollars to Japanese yen'")
        print("• 'Show me exchange rates for British pound'")
        print("• 'What is 50 euros in Canadian dollars?'")
        print("• 'Get the latest USD to GBP exchange rate'")
        print("\nPress 'q' and Enter anytime to quit.")
        print("=" * 60)
        
        # The voice module will handle communication with the agent directly
        # No need for manual tool handling since we're using auto function calls
        
        # Start the voice conversation
        await av.connect()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        print("\n👋 Demo completed!")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🎙️ VOICE-CONTROLLED CURRENCY EXCHANGE ASSISTANT")
    print("Features: Get exchange rates via API with voice commands")
    print("=" * 60)
    
    # Run the main demo
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Demo interrupted by user")
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
