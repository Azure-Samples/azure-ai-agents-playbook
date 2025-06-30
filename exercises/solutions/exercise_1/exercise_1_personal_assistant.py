import asyncio
from http import client
import os
from datetime import datetime
import random
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential
from semantic_kernel.agents import AzureAIAgent
from semantic_kernel.functions import kernel_function

class PersonalAssistantPlugin:
    @kernel_function(description="Get current date and time")
    def get_current_time(self) -> Annotated[str, "Current date and time"]:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @kernel_function(description="Calculate basic math operations")
    def calculate(
        self, 
        operation: Annotated[str, "Math operation like '25 * 4' or '10 + 5'"]
    ) -> Annotated[str, "Calculation result"]:
        return str(eval(operation))
    
    @kernel_function(description="Get a motivational quote")
    def get_quote(self) -> Annotated[str, "A motivational quote"]:
        quotes = [
            "The only way to do great work is to love what you do. - Steve Jobs",
            "Innovation distinguishes between a leader and a follower. - Steve Jobs",
            "Stay hungry, stay foolish. - Steve Jobs",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
        ]
        return random.choice(quotes)

async def main():
    # Create the agent
    client = AzureAIAgent.create_client(
        credential=DefaultAzureCredential(), 
        endpoint=os.environ.get("PROJECT_ENDPOINT")
    )
    
    try:
        async with client:
            agent_definition = await client.agents.create_agent(
                model=os.environ.get("MODEL_DEPLOYMENT_NAME"),
                name="personal-assistant",
                instructions="You are a friendly personal assistant that helps with daily tasks."
            )
            
            agent = AzureAIAgent(
                client=client,
                definition=agent_definition,
                plugins=[PersonalAssistantPlugin()]
            )
            
            # Test questions
            questions = [
                "What time is it?",
                "Calculate 25 * 4",
                "Give me a motivational quote"
            ]
            
            # Have conversations
            for question in questions:
                print(f"User: {question}")
                response = await agent.get_response(question)
                print(f"Assistant: {response}\n")
            
            # Cleanup
            await client.agents.delete_agent(agent.id)

    finally:
        await client.close()

if __name__ == "__main__":
    asyncio.run(main())
