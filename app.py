import streamlit as st
import os
from dotenv import load_dotenv
from pricing_agent import PricingAgent

# Load environment variables (API Key)
load_dotenv()

st.set_page_config(page_title="AI Strategic Pricing Agent", layout="wide")

st.title("🤖 Strategic Pricing Agent")
st.markdown("""
This agent uses **Agentic AI** and **Chain-of-Thought Reasoning** to optimize 
product pricing while balancing margins and market competition.
""")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Groq API Key", type="password", 
                             value=os.getenv("GROQ_API_KEY", ""))
    
    st.divider()
    st.header("Product Data")
    cost = st.number_input("Cost Price ($)", min_value=0.0, value=400.0)
    current = st.number_input("Current Price ($)", min_value=0.0, value=599.0)
    target_margin = st.slider("Target Margin (%)", 0, 100, 25)
    competitor = st.number_input("Competitor Price ($)", min_value=0.0, value=579.0)
    elasticity = st.selectbox("Price Elasticity", ["Low", "Medium", "High"])

# Main execution
if st.button("Run Strategic Analysis"):
    if not api_key:
        st.error("Please provide a Groq API Key to continue.")
    else:
        try:
            agent = PricingAgent(api_key=api_key)
            with st.spinner("Agent is reasoning..."):
                recommendation = agent.get_price_recommendation(
                    cost, current, target_margin, competitor, elasticity
                )
            
            st.subheader("Analysis & Recommendation")
            st.markdown(recommendation)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")