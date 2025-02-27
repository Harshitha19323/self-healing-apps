import subprocess
import time
import logging

# Configure logging
logging.basicConfig(filename="self_healing.log", level=logging.INFO, 
                    format="%(asctime)s - %(levelname)s - %(message)s")

# Application command (Replace with your actual app/script)
APP_COMMAND = ["python", "app.py"]  # Modify based on your application

def start_application():
    """Starts the application and returns the process."""
    logging.info("Starting application...")
    return subprocess.Popen(APP_COMMAND)

def monitor_application():
    """Monitors the application and restarts it if it crashes."""
    process = start_application()
    
    while True:
        try:
            # Check if process is still running
            process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            # Process is still running
            time.sleep(5)
            continue

        # Process terminated, restart it
        logging.warning("Application crashed. Restarting...")
        process = start_application()
        time.sleep(2)  # Small delay before restarting

if __name__ == "__main__":
    logging.info("Self-healing monitor started.")
    monitor_application()
