from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
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
memory = ConversationBufferMemory(
    chat_memory=FileChatMessageHistory("messages.json"),
    memory_key="messages",
    return_messages=True,
)
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

while True:
    content = input(">> ")
    result = chain({"content": content})
    print(result["text"])
