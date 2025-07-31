from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

def get_arxiv_tool():
    wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=300)
    return ArxivQueryRun(api_wrapper=wrapper)
