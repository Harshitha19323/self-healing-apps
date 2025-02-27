import psutil

APP_NAME = "app.py"  # Name of the script you want to monitor

def is_running():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        if APP_NAME in process.info['name']:
            return True
    return False

if __name__ == "__main__":
    print("App Status:", "Running ✅" if is_running() else "Stopped ❌")
