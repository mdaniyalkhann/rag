from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage
from dotenv import load_dotenv

load_dotenv(override=True)

chat_template = ChatPromptTemplate(
    messages=[
        SystemMessage(content="You respond only in the JSON format"),
        HumanMessagePromptTemplate.from_template(
            "Top {n} countries in {area} by population"
        ),
    ]
)

messages = chat_template.format(n='2', area="Asia")
llm = ChatOpenAI()
output = llm.invoke(messages)
print(output.content)
