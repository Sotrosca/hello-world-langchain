from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = ChatOllama(
    model="gpt-oss:120b-cloud",
    temperature=0.8,
    num_predict=256,
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]

# Run the agent
agent.invoke(messages)
