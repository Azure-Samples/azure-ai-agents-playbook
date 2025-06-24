# Import everything we need
import os
import asyncio
import json
import requests
import random
from datetime import datetime
from typing import Any, Dict, Annotated
from semantic_kernel.functions import kernel_function
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion



# Weather Plugin
class WeatherPlugin:
    """A plugin for getting weather information."""
    
    @kernel_function(
        description="Gets the current weather for a city",
        name="get_weather"
    )
    def get_weather(
        self, 
        city: Annotated[str, "The name of the city to get weather for"]
    ) -> Annotated[str, "The current weather information"]:
        """
        Gets the current weather for a city (mock implementation).
        """
        # In a real implementation, you'd call a weather API
        weather_options = [
            f"Sunny and 72°F in {city}",
            f"Partly cloudy and 68°F in {city}", 
            f"Rainy and 61°F in {city}",
            f"Overcast and 65°F in {city}"
        ]
        weather = random.choice(weather_options)
        print(f"🌤️ Weather check: {weather}")
        return weather

# Random Number Plugin
class RandomPlugin:
    """A plugin for generating random numbers and choices."""
    
    @kernel_function(
        description="Generates a random number between min and max values",
        name="generate_random_number"
    )
    def generate_random_number(
        self, 
        min_val: Annotated[int, "The minimum value (inclusive)"], 
        max_val: Annotated[int, "The maximum value (inclusive)"]
    ) -> Annotated[int, "A random number between min and max"]:
        """
        Generates a random number between min and max values.
        """
        result = random.randint(min_val, max_val)
        print(f"🎲 Generated random number: {result} (between {min_val} and {max_val})")
        return result

# DateTime Plugin
class DateTimePlugin:
    """A plugin for date and time operations."""
    
    @kernel_function(
        description="Gets the current date and time",
        name="get_current_datetime"
    )
    def get_current_datetime(self) -> Annotated[str, "The current date and time"]:
        """
        Gets the current date and time.
        """
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"🕐 Current time: {formatted_time}")
        return formatted_time

# Text Analysis Plugin
class TextAnalysisPlugin:
    """A plugin for analyzing text content."""
    
    @kernel_function(
        description="Analyzes text and returns statistics",
        name="analyze_text"
    )
    def analyze_text(
        self, 
        text: Annotated[str, "The text to analyze"]
    ) -> Annotated[str, "JSON string containing text analysis results"]:
        """
        Analyzes text and returns statistics.
        """
        words = text.split()
        analysis = {
            "character_count": len(text),
            "word_count": len(words),
            "sentence_count": text.count('.') + text.count('!') + text.count('?'),
            "average_word_length": round(sum(len(word) for word in words) / len(words), 2) if words else 0
        }
        print(f"📊 Text analysis complete: {analysis}")
        return json.dumps(analysis)

# RAG Plugin
class RAGPlugin:
    """A plugin for retrieving context from BMW 320i car insurance policy documents."""
    
    @kernel_function(
        description="Retrieves context about BMW 320i car insurance policy",
        name="get_insurance_context"
    )
    async def get_insurance_context(
        self, 
        query: Annotated[str, "The question about BMW 320i insurance policy"]
    ) -> Annotated[str, "The retrieved context from insurance documents"]:
        """
        Retrieves context about BMW 320i car insurance policy.
        """

        ### IMPORTANT ### 
        # An SK agent is used here to simulate a retrieval-augmented generation (RAG) process only.
        # In a real-world scenario, you would integrate with a document retrieval system or knowledge base.
        ### IMPORTANT ### 

        system_message = """You are a BMW 320i car insurance knowledge base. Return relevant context for queries about coverage, premiums, deductibles, and claims. Keep responses concise and factual."""
        
        rag_agent = ChatCompletionAgent(
            id="RAGAgent",
            name="RAGAgent", 
            instructions=system_message,
            description="This agent returns the context retrieved from insurance documents.",
            service=AzureChatCompletion(),
        )
        
        async for response in rag_agent.invoke(messages=query):
            content = response.content
            print(f"🔍 Insurance Agent / RAG context retrieved for: {query}")
            return content

# NL2SQL Plugin
class NL2SQLPlugin:
    """A plugin for retrieving banking transaction data via SQL queries."""
    
    @kernel_function(
        description="Converts natural language to SQL and returns banking transaction results",
        name="get_banking_data"
    )
    async def get_banking_data(
        self, 
        query: Annotated[str, "The question about banking transactions"]
    ) -> Annotated[str, "The retrieved banking transaction data"]:
        """
        Converts natural language to SQL and returns banking transaction results.
        """

        ### IMPORTANT ### 
        # An SK agent is used here to simulate a natural language to SQL (NL2SQL) process.
        # In a real-world scenario, you would integrate with a SQL database or service.
        ### IMPORTANT ### 

        system_message = """You are a banking transaction database. Return fake transaction data for queries about account balances, spending, deposits, and transaction history. Format as simple JSON or text."""
        
        sql_agent = ChatCompletionAgent(
            id="SQLAgent",
            name="SQLAgent",
            instructions=system_message,
            description="This agent returns transaction data from SQL database.",
            service=AzureChatCompletion(),
        )
        
        async for response in sql_agent.invoke(messages=query):
            content = response.content
            print(f"💳 Banking Agent / NL2SQL data retrieved for: {query}")
            return content

# Cosmos Plugin
class CosmosPlugin:
    """A plugin for retrieving multimodal sales analysis documents from Cosmos DB."""
    
    @kernel_function(
        description="Retrieves sales analysis data for smart city IoT solutions from Cosmos DB",
        name="get_sales_analysis"
    )
    async def get_sales_analysis(
        self, 
        query: Annotated[str, "The question about last year's sales analysis"]
    ) -> Annotated[str, "The retrieved sales analysis documents in JSON format"]:
        """
        Retrieves sales analysis data for smart city IoT solutions from Cosmos DB.
        """

        ### IMPORTANT ###
        # An SK agent is used here to simulate a retrieval process from Cosmos DB.
        # In a real-world scenario, you would integrate with Azure Cosmos DB or a similar service.
        ### IMPORTANT ###

        system_message = """You are a Cosmos DB containing multimodal sales analysis documents for a smart city IoT solutions company. Return fake JSON data about sales metrics, product performance, and market analysis from last year."""
        
        cosmos_agent = ChatCompletionAgent(
            id="CosmosAgent",
            name="CosmosAgent",
            instructions=system_message,
            description="This agent returns sales analysis documents from Cosmos DB.",
            service=AzureChatCompletion(),
        )
        
        async for response in cosmos_agent.invoke(messages=query):
            content = response.content
            print(f"📊 Sales Agent / Cosmos analysis retrieved for: {query}")
            return content

# Create plugin instances
weather_plugin = WeatherPlugin()
random_plugin = RandomPlugin()
datetime_plugin = DateTimePlugin()
text_analysis_plugin = TextAnalysisPlugin()
rag_plugin = RAGPlugin()
nl2sql_plugin = NL2SQLPlugin()
cosmos_plugin = CosmosPlugin()

print("✅ All utility plugins defined!")
print("🔧 Available plugins: Weather, Random, DateTime, TextAnalysis, RAG, NL2SQL, Cosmos")