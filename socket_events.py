import subprocess

def register_socket_events(socketio):
    @socketio.on('run_script')
    def handle_run_script(data):
        process = subprocess.Popen(
            ['python', 'SimplerunV2.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        for line in process.stdout:
            socketio.emit('script_output', {'output': line.strip()})
        for line in process.stderr:
            socketio.emit('script_output', {'output': f"ERROR: {line.strip()}"})
        process.wait()
        socketio.emit('script_done', {'status': 'finished'})
