
from flask import Flask
import subprocess
import sys
import keyboard
import pyautogui

app = Flask(__name__)

# Launch applications
@app.route('/launch/<app_name>')
def launch_app(app_name):
    apps = {
        "calculator": "calc",
        "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
        "camera": "start microsoft.windows.camera:",
    }
    app_path = apps.get(app_name.lower())

    if app_path:
        try:
            subprocess.Popen(app_path if sys.platform == "win32" else ["open", app_path])
            return f"Launching {app_name}..."
        except Exception as e:
            return f"Failed to launch {app_name}: {e}"
    return "Application not found."

# Media control functions
@app.route('/media/play_pause')
def play_pause():
    try:
        keyboard.press_and_release('play/pause media')
        return "Toggled play/pause."
    except Exception as e:
        return f"Error in play/pause: {e}"

@app.route('/media/next')
def next_track():
    try:
        keyboard.press_and_release('next track')
        return "Skipped to next track."
    except Exception as e:
        return f"Error in next track: {e}"

@app.route('/media/previous')
def previous_track():
    try:
        keyboard.press_and_release('previous track')
        return "Went to previous track."
    except Exception as e:
        return f"Error in previous track: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make it accessible on your local network
