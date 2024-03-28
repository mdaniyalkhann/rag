from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationSummaryBufferMemory
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate(
    input_variables=["contnet"],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}"),
    ],
)

llm = ChatOpenAI()
memory = ConversationSummaryBufferMemory(
    memory_key="messages",
    return_messages=True,
    llm=llm,
)
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
