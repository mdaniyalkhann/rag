from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI()
embeddings = OpenAIEmbeddings()


# text_splitter = CharacterTextSplitter(separator="\n", chunk_size=200, chunk_overlap=0)

# loader = TextLoader("facts.txt")
# docs = loader.load_and_split(text_splitter=text_splitter)

# db = Chroma.from_documents(docs, embedding=embeddings, persist_directory="emb")


db = Chroma(persist_directory="emb", embedding_function=embeddings)
retriever = db.as_retriever()

chain = RetrievalQA.from_chain_type(llm=chat, retriever=retriever, chain_type="stuff") # other are "refine", "map_reduce", "map_rerank"

result = chain.run("What is longest word in english?")

print(result)
