import asyncio
import os
import json
from typing import Annotated

from azure.ai.agents import AgentsClient
from azure.ai.agents.models import OpenApiTool, OpenApiAnonymousAuthDetails
from azure.identity import DefaultAzureCredential

# Import voice module
from voice import AgentVoice


# Alpha Vantage API key for stock market data
# Replace with your actual API key
# You can get a free API key from https://www.alphavantage.co/support/#api-key
alphavantage_api_key = "<you_need_to_replace_with_your_api_key>"


async def create_stock_agent():
    model_deployment_name = os.environ.get("MODEL_DEPLOYMENT_NAME")
    endpoint = os.environ.get("PROJECT_ENDPOINT")
    
    credential = DefaultAzureCredential()
    agents_client = AgentsClient(endpoint=endpoint, credential=credential)
    
    # Load the stock market OpenAPI specification
    stock_spec_path = os.path.join("openapi_files", "stock_market.json")
    
    with open(stock_spec_path, "r") as f:
        stock_openapi_spec = json.loads(f.read())
    
    # Create OpenAPI tool for stock market data
    auth = OpenApiAnonymousAuthDetails()
    
    stock_tool = OpenApiTool(
        name="stock_market",
        spec=stock_openapi_spec,
        description="Get real-time stock market data from Alpha Vantage API",
        auth=auth
    )
    
    print("📈 Stock market OpenAPI tool created")
    print(f"Available operations: {len(stock_tool.definitions)}")
    
    with agents_client:
        agent = agents_client.create_agent(
            model=model_deployment_name,
            name="voice_stock_agent",
            instructions=f"You are a voice-controlled stock market assistant. Use the stock market API to get real-time stock prices and data. Always provide clear explanations of the stock information. Your responses are SUPER concise. Please use the Alpha Vantage API key: {alphavantage_api_key} for authentication. Use 'TIME_SERIES_DAILY' as the default function for daily stock data.",
            tools=stock_tool.definitions
        )
        
        print(f"🤖 Created voice stock agent: {agent.name}")
        print(f"🔧 Agent has stock market capabilities")
        print(f"🆔 Agent ID: {agent.id}")
    
    return agent, agents_client

async def main():
    print("🎙️ Starting Voice-Enabled Stock Market Agent Demo")
    print("=" * 60)
    
    # Create the stock agent
    print("Creating voice stock agent with market data integration...")
    agent, agents_client = await create_stock_agent()
    
    # Create voice interface with the agent
    print("\n🎤 Setting up voice interface...")
    av = AgentVoice(agent_id=agent.id)
    
    print("\n🗣️ Voice interface ready!")
    print("Sample voice commands you can try:")
    print("• 'What's the current price of Apple stock?'")
    print("• 'Show me Microsoft's stock performance this week'")
    print("• 'Compare Tesla and Ford stock prices'")
    print("• 'Get IBM stock history'")
    print("\nPress 'q' and Enter anytime to quit.")
    print("=" * 60)
    
    # Start the voice conversation
    await av.connect()
    
    print("\n👋 Demo completed!")

if __name__ == "__main__":
    asyncio.run(main())
