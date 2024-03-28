from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI()
prompt = "Write song about the Moon and Raven."

for chunk in llm.stream(prompt):
    print(chunk.content, end="", flush=True)
