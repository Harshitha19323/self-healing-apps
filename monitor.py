import subprocess
import time
import logging

# Configure logging
logging.basicConfig(filename="self_healing.log", level=logging.INFO, format="%(asctime)s - %(message)s")

APP_COMMAND = ["python", "app.py"]  # Change this to the script you want to monitor

def start_application():
    """Start the monitored application and restart it if it crashes."""
    while True:
        logging.info("Starting application...")
        process = subprocess.Popen(APP_COMMAND)

        process.wait()  # Wait for process to exit
        logging.warning(f"Application crashed with exit code {process.returncode}. Restarting...")

        time.sleep(2)  # Short delay before restart

if __name__ == "__main__":
    start_application()
