from langchain.chat_models import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate(
    input_variables=["contnet"],
    messages=[
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

llm = ChatOpenAI()
chain = LLMChain(llm=llm, prompt=prompt)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
