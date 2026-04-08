from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Server is running"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '').lower()

    print("Question:", question)

    if "evaluate" in question:
        answer = "The assignment shows basic understanding. Some concepts are correct but more explanation is needed."

    elif "summary" in question:
        answer = "This assignment explains the topic in a simple way covering main points."

    elif "improve" in question:
        answer = "The student should add more examples and explain concepts in detail."

    else:
        answer = "Teacher Copilot suggests reviewing clarity and concept understanding."

    return jsonify({'answer': answer})

if __name__ == "__main__":
    app.run(debug=True)