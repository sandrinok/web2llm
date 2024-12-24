from flask import Flask
from flask_socketio import SocketIO
from web_routes import register_routes
from socket_events import register_socket_events
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
socketio = SocketIO(app)

# Registreer routes en socket-evenementen
register_routes(app)
register_socket_events(socketio)

if __name__ == "__main__":
    print("Starting Flask web server on http://localhost:8188...")
    socketio.run(app, host="localhost", port=8188, debug=True)
