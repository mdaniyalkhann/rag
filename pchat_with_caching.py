from langchain_openai import OpenAI
from langchain.globals import set_llm_cache
from langchain.cache import InMemoryCache
from dotenv import load_dotenv;

load_dotenv(override=True);

llm = OpenAI()
set_llm_cache(InMemoryCache())
prompt = 'Tell me a joke that toddler can understand.'

print(llm.invoke(prompt))
print(llm.invoke(prompt))