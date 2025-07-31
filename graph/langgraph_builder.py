from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from state.schema import State
from tools.arxiv_tool import get_arxiv_tool
from tools.wikipedia_tool import get_wikipedia_tool
from tools.weather_tool import get_weather
from tools.real_estate_tool import get_real_estate_info
from agents.chatbot_agent import get_llm

def build_graph():
    arxiv_tool = get_arxiv_tool()
    wiki_tool = get_wikipedia_tool()
    
    tools = [arxiv_tool, wiki_tool,get_weather,get_real_estate_info]

    llm = get_llm().bind_tools(tools=tools)

    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}

    graph_builder = StateGraph(State)
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_node("tools", ToolNode(tools=tools))
    graph_builder.add_conditional_edges("chatbot", tools_condition)

    return graph_builder.compile()
