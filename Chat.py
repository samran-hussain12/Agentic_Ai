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



# Import libraries
from langchain import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Initialize OpenAI model
model = OpenAI(api_key="your_api_key")

# Create a prompt template
prompt = PromptTemplate(template="What is the capital of {country}?")

# Create a chain
chain = LLMChain(llm=model, prompt=prompt)

# Use the chain
response = chain.run(country="France")
print(response)