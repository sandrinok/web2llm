import os
import subprocess
from flask import request, jsonify, send_from_directory
from config import VEN_NAME

# Functie om de scraper te draaien
def run_scraper(script_name, param=""):
    try:
        result = subprocess.run(
            [os.path.join(VEN_NAME, 'Scripts', 'python'), script_name, param],
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Script execution failed: {e.stderr}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error: {str(e)}")

# Functie om routes te registreren
def register_routes(app):
    html_filename = "index.html"

    @app.route("/")
    def home():
        # Serve het externe HTML-bestand
        return send_from_directory('.', html_filename)

    @app.route('/run-script', methods=['POST'])
    def run_script_route():
        data = request.json
        param = data.get('input', '')

        try:
            output = run_scraper('SimplerunV2.py', param)
            return jsonify({'output': output})
        except RuntimeError as e:
            return jsonify({'error': str(e)}), 500
