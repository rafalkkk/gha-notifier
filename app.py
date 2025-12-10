from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Pozwala na zapytania z innych domen

last_message = ""

@app.route('/api/message', methods=['POST'])
def receive_message():
    global last_message
    data = request.get_json()
    message = data.get('message', '')
    last_message = message
    return jsonify({'status': 'Message received'}), 200

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': last_message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
