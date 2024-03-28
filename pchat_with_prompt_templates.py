from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv(override=True)

template = """You are experience virologist.
Write 1 sentence about the following virus {virus} in {language}
"""

prompt_template = PromptTemplate(
    template=template, input_variables=["virus", "language"]
)
prompt = prompt_template.format(virus="SARS-CoV-2", language="English")

llm = ChatOpenAI(temperature=0)
output = llm.invoke(prompt)
print(output.content)
