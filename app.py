from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

# Store the last message to send to new clients
last_message = ""

@app.route('/api/message', methods=['POST'])
def receive_message():
    global last_message
    data = request.get_json()
    message = data.get('message', '')
    last_message = message
    # Broadcast message to all connected clients
    socketio.emit('new_message', {'message': message})
    return jsonify({'status': 'Message broadcasted'}), 200

@socketio.on('connect')
def handle_connect():
    # Send the last message to the newly connected client
    emit('new_message', {'message': last_message})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
