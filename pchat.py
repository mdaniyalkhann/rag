from langchain_openai import ChatOpenAI
from langchain.schema.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv;

load_dotenv();

llm = ChatOpenAI()
# output = llm.invoke("Explain quantum mechanics in one sentence?")
# print(output)

messages = [
    SystemMessage(content="You are physicist and respond only in German."),
    HumanMessage(content="Explain quantum mechanics in one sentence."),
]

output = llm.invoke(messages)
print(output)