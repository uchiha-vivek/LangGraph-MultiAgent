from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

def get_wikipedia_tool():
    wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=300)
    return WikipediaQueryRun(api_wrapper=wrapper)
