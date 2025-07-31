import pytest
from graph.langgraph_builder import build_graph

@pytest.fixture
def langgraph_agent():
    return build_graph()

def test_diffusion_model_query_triggers_tools(langgraph_agent):
    user_input = "Explain Diffusion Models in AI and list some recent research papers."
    events = list(
        langgraph_agent.stream({"messages": [("user", user_input)]}, stream_mode="values")
    )

    assert events, "No events were returned by the graph stream"

    final_message = events[-1]["messages"][-1].content.lower()

    # Check if the response includes discussion of diffusion models
    assert any(kw in final_message for kw in ["diffusion model", "denoising"]), \
        "Expected content about Diffusion Models not found in final message"

    # Check for patterns indicating paper metadata
    has_paper_metadata = any(
        kw in final_message for kw in ["published:", "title:", "authors:", "summary:"]
    )
    assert has_paper_metadata, "Expected mention of recent research papers not found in final message"



def test_tool_usage_verbose(langgraph_agent, capsys):
    user_input = "Tell me who Elon Musk is and give recent papers about SpaceX."
    events = list(
        langgraph_agent.stream({"messages": [("user", user_input)]}, stream_mode="values")
    )

    assert len(events) > 0, "No output from graph for Elon Musk + SpaceX query"
    last = events[-1]["messages"][-1].content.lower()
    assert "elon musk" in last or "spacex" in last, \
        "Expected content related to Elon Musk or SpaceX not found"
