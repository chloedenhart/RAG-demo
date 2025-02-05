# to load all PDF files in a directory
from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_docs():
    loader = PyPDFDirectoryLoader("LLM_Education/")
    knowledge_base = loader.load()
    return knowledge_base
