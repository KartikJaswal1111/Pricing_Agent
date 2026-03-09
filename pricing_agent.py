"""
pricing_agent.py: Core logic for the Strategic Pricing Agent.
Extracted and modularized from Assignment 1.
"""

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
import os

class PricingAgent:
    """
    A seasoned pricing expert agent that provides data-driven recommendations
    using Chain-of-Thought reasoning.
    """
    
    def __init__(self, api_key: str, model: str = "llama-3.1-8b-instant"):
        """Initializes the LLM and prompt templates."""
        self.llm = ChatGroq(
            model=model,
            api_key=api_key,
            temperature=0.2,
            max_tokens=1000
        )
        
        self.system_message = SystemMessage(content="""
            You are a seasoned pricing expert. Your goal is to provide data-driven 
            price recommendations and clear, concise reasoning based on input parameters.
        """)
        
        self.pricing_template = PromptTemplate(
            input_variables=["cost_price", "current_price", "target_margin", 
                             "competitor_price", "price_elasticity"],
            template="""Given the following information:
    Cost Price: ${cost_price}
    Current Price: ${current_price}
    Target Margin: {target_margin}%
    Competitor Price: ${competitor_price}
    Price Elasticity: {price_elasticity}

    Please follow these steps to provide a detailed pricing recommendation:
    1. Calculate the minimum viable price based on the target margin.
    2. Analyze current price and competitor's price for competitive positioning.
    3. Evaluate the impact of price elasticity on potential demand changes.
    4. Recommend an optimal price, explaining your reasoning considering all factors.
    """
        )

    def get_price_recommendation(self, cost_price, current_price, target_margin, 
                                 competitor_price, price_elasticity):
        """Generates a detailed price recommendation using CoT."""
        messages = [
            self.system_message,
            HumanMessage(content=self.pricing_template.format(
                cost_price=cost_price,
                current_price=current_price,
                target_margin=target_margin,
                competitor_price=competitor_price,
                price_elasticity=price_elasticity
            ))
        ]
        
        response = self.llm.invoke(messages)
        return response.content