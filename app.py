from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

last_message = ""

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/message', methods=['POST'])
def receive_message():
    global last_message
    data = request.get_json()
    last_message = data.get('message', '')
    return jsonify({'status': 'Message received'}), 200

@app.route('/api/message', methods=['GET'])
def get_message():
    return jsonify({'message': last_message}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
