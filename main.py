from graph.langgraph_builder import build_graph

if __name__ == "__main__":
    graph = build_graph()
    
    user_input = "Explain RLHF and mention recent research papers about it."
    events = graph.stream(
        {"messages": [("user", user_input)]}, stream_mode="values"
    )

    for event in events:
        event["messages"][-1].pretty_print()
