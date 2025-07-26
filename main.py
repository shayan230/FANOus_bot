from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Message received:", data)

    if 'message' in data and 'text' in data['message']:
        user_message = data['message']['text']
        if user_message == '/start':
            return jsonify({'text': 'ربات فانوس بزودی در دسترس شما قرار می‌گیرد.'})

    return jsonify({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
