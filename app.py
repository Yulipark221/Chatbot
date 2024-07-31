from flask import Flask, request, jsonify, render_template
from chatbot import chatbot

app = Flask(__name__)

@app.route('/')
def index():
    """Render the HTML page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat requests."""
    user_message = request.json.get('message')
    if user_message:
        response = chatbot.respond(user_message)
        return jsonify({'response': response})
    return jsonify({'response': 'I didn\'t understand your request.'})

if __name__ == '__main__':
    app.run(debug=True)
