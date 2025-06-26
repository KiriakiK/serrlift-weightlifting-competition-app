from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO, emit

app = Flask(__name__, static_folder='serrlift1')
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/men')
def control_men():
    return send_from_directory('serrlift1', 'control_Men.html')

@app.route('/women')
def control_women():
    return send_from_directory('serrlift1', 'control_Women.html')

@app.route('/screen')
def screen():
    return send_from_directory('serrlift1', 'screen.html')

@app.route('/results')
def results():
    return send_from_directory('serrlift1', 'warmupresults.html')

@app.route('/socket.io.min.js')
def serve_socketio():
    return send_from_directory('serrlift1', 'socket.io.min.js')

@app.route('/beep_short.ogg')
def serve_beep():
    return send_from_directory('serrlift1', 'beep_short.ogg')

@socketio.on('state_update')
def handle_state_update(data):
    emit('state_broadcast', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    print("Starting SocketIO server on port 5000...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)

