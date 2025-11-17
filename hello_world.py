from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-v3.1:671b-cloud",
    validate_model_on_init=True,
    temperature=0.8,
    num_predict=256,
    # other params ...
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
model.invoke(messages)
