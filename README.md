# 🤖 LangGraph AI Agentic System:

This project is a **modular LangGraph-based agentic system** built with [LangChain](https://github.com/langchain-ai/langchain), [LangGraph](https://github.com/langchain-ai/langgraph), and Azure OpenAI . 

---

## 🚀 Purpose

The goal of this project is to demonstrate how **AI agents** can be combined with **external tools** and orchestrated using **LangGraph's workflow-based graph**. Specifically, it:
- Explains technical topics like how different research papers can be searched and queried .
- Fetches relevant academic papers using **Arxiv**
- Retrieves summaries and definitions using **Wikipedia**
- Makes use of **LangChain's agentic tooling** and **LangGraph's conditional flows**

---

### Setup


Clone the repository
```bash
git clone https://github.com/uchiha-vivek/LangGraph-MultiAgent.git
```

Navigate to the directory
```bash
cd LangGraph-MultiAgent
```

Make virtual environment (Here for Windows)
```bash
python -m venv venv
```

Activate the virtual environment
```bash
venv\Scripts\activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run command
```bash
python main.py
```


After server is running successfully on localhost:5000 ,test the api in curl or postman :
```bash
curl -X POST http://localhost:5000/api/ask-ai \
     -H "Content-Type: application/json" \
     -d '{"message": "Explain Diffusion Models in AI and list some recent research papers."}'

```


If you just want to run the agent :

```bash
python run.py
```

For testing the agent , run :
```bash
pytest tests/
```

Contributor :  Vivek Sharma --(Founding AI Engineer) 
