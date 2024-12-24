import os
import subprocess
from config import VEN_NAME

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
