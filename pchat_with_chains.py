from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv

load_dotenv(override=True)

llm = ChatOpenAI()
template = """You are experience virologist.
Write 1 sentence about the following virus {virus} in {language}
"""

prompt_template = PromptTemplate(
    template=template, input_variables=["virus", "language"]
)

chain = LLMChain(llm=llm, prompt=prompt_template)
output = chain.invoke(input={"virus": "Covid", "language": "English"})
print(output)
