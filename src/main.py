from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join_room')
def handle_join_room(data):
    username = data['username']
    print(username)
    room = data['room']
    join_room(room)
    socketio.emit('joined_room', {'username': username, 'room': room}, room=room)

@socketio.on('leave_room')
def handle_leave_room(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    socketio.emit('left_room', {'username': username, 'room': room}, room=room)

@socketio.on('send_message')
def handle_send_message(data):
    username = data['username']
    room = data['room']
    message = data['message']
    socketio.emit('receive_message', {'username': username, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
