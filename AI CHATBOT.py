import openai
from flask import Flask, render_template, request, jsonify

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

app = Flask(__name__)

# Initialize the conversation with a system message
conversation = [
    {
        "role": "system",
        "content": "You are OpenAI Chatgpt"
    }
]


@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    assistant_reply = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": assistant_reply})

    return jsonify({"assistant_reply": assistant_reply})

if __name__ == '__main__':
    app.run(debug=True)
