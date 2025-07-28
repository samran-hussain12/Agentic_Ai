# LangChain libraries
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# For document loading
from langchain.document_loaders import TextLoader

# For text splitting
from langchain.text_splitter import RecursiveCharacterTextSplitter

# For retrieval
from langchain.retrievers import VectorStoreRetriever