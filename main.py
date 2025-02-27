# Note: You'll need to install agno first in Replit
# In the Replit shell, run: pip install agno
# Also, set your OPENAI_API_KEY in Replit Secrets/Environment Variables

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# Greeting Agent: Welcomes customers and identifies their needs
greeting_agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),  # Using a lightweight model
    description="You are a friendly customer support greeter",
    instructions=[
        "Welcome the customer warmly",
        "Ask how you can assist them today",
        "Keep responses short and professional",
        "If they state a problem, pass it to the support agent"
    ],
    markdown=True
)

# Support Agent: Provides detailed assistance
support_agent = Agent(
    model=OpenAIChat(id="gpt-4o"),  # More powerful model for detailed responses
    tools=[DuckDuckGoTools()],  # Web search capability
    description="You are a knowledgeable customer support specialist",
    instructions=[
        "Provide helpful and accurate responses to customer questions",
        "Use web search if needed to find up-to-date information",
        "Be polite and professional",
        "Offer practical solutions or next steps"
    ],
    show_tool_calls=True,
    markdown=True
)

# Simple function to simulate customer interaction
def handle_customer_query(query):
    # Step 1: Greeting Agent responds first
    print("=== Greeting Agent ===")
    greeting_response = greeting_agent.print_response(query, stream=True)

    # Step 2: If query contains a specific question/problem, pass to Support Agent
    if "?" in query or "help" in query.lower() or "problem" in query.lower():
        print("\n=== Support Agent ===")
        support_response = support_agent.print_response(query, stream=True)
    else:
        print("\nPlease tell me how I can assist you further!")

# Test the customer support team
if __name__ == "__main__":
    # Example customer queries
    test_queries = [
        "Hi, I'm having trouble with my account",
        "Can you tell me about your refund policy?",
        "Hello, I need help resetting my password",
        "How do I fix a Python TypeError?"
    ]

    for query in test_queries:
        print(f"\nCustomer Query: {query}")
        handle_customer_query(query)
        print("-" * 50)