# 🤖 Strategic AI Pricing Agent

## 📈 Business Impact
Pricing is one of the most powerful levers for profitability. This project solves 
the **"Margin vs. Market" conflict**—where companies often lose profit by either 
undercutting themselves or pricing themselves out of the market. 

By using **Agentic AI**, this tool:
- **Protects Margins:** Ensures every recommendation meets the target profitability.
- **Market Sensitivity:** Adjusts dynamically to competitor benchmarks.
- **Data-Driven Logic:** Replaces "gut-feel" pricing with transparent verbal reasoning.

## 🛠 Technical Implementation
This application transitions from experimental code into a scalable, 
containerized microservice.

- **Agentic Logic:** Built with **LangChain**, utilizing **Chain-of-Thought (CoT)** prompting to ensure the AI "thinks" through calculations before recommending a price.
- **High-Speed Inference:** Powered by **Groq** (Llama 3.1) for near-instant 
  strategic reasoning.
- **Interactive UI:** A **Streamlit** dashboard for real-time scenario testing.
- **Containerization:** **Dockerized** to ensure consistent deployment across any environment.

## 🚀 Getting Started

### Using Docker (Recommended)
1. Build the image: `docker build -t pricing-agent .`
2. Run the container: `docker run -p 8501:8501 pricing-agent`

### Local Development
1. `pip install -r requirements.txt`
2. Create a `.env` file with your `GROQ_API_KEY`.
3. `streamlit run app.py`

## 🧠 Learning & Challenges
- **The Reasoning Gap:** Moving from basic prompts to CoT significantly improved the 
  accuracy of mathematical margin calculations.
- **Production Alignment:** Transitioning logic from a notebook to a modular class-based 
  system ensures the code is extensible and maintainable.