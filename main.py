from flask import Flask
from routes.agent_route import ai_bp

app = Flask(__name__)
app.register_blueprint(ai_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
