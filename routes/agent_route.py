from flask import Blueprint, request, jsonify
from graph.langgraph_builder import build_graph

ai_bp = Blueprint("ai_routes", __name__)

@ai_bp.route("/ask-ai", methods=["POST"])
def ask_ai():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Missing 'message' field"}), 400

    graph = build_graph()
    events = graph.stream(
        {"messages": [("user", user_input)]}, stream_mode="values"
    )

    responses = []
    for event in events:
        msg = event["messages"][-1].content
        responses.append(msg)

    return jsonify({"responses": responses})
