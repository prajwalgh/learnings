# from flask import Flask, jsonify
# import pyautogui
# import time
#
# app = Flask(__name__)
#
# # Define the functions to control YouTube playback
# def play_pause():
#     # Spacebar toggles play/pause on YouTube
#     pyautogui.press('space')
#
# def next_video():
#     # 'Shift + N' is the shortcut for next video on YouTube
#     pyautogui.hotkey('shift', 'n')
#
# def previous_video():
#     # 'Shift + P' is the shortcut for previous video on YouTube
#     pyautogui.hotkey('shift', 'p')
#
# @app.route('/play', methods=['POST'])
# def play():
#     play_pause()
#     return jsonify({"message": "Toggled play/pause on YouTube."})
#
# @app.route('/next', methods=['POST'])
# def next_vid():
#     next_video()
#     return jsonify({"message": "Skipped to next video on YouTube."})
#
# @app.route('/prev', methods=['POST'])
# def prev_vid():
#     previous_video()
#     return jsonify({"message": "Went to previous video on YouTube."})
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
import keyboard
import time
import  ctypes
import pyautogui

def play_pause():
    # Simulate the play/pause media key
    keyboard.press_and_release('play/pause media')
    print("Toggled play/pause.")
def next_track():
    # Simulate the next track media key
    keyboard.press_and_release('next track')
    print("Skipped to next track.")
def previous_track():
    # Simulate the previous track media key
    keyboard.press_and_release('previous track')
    print("Went to previous track.")


# Example usage
if __name__ == "__main__":
    while True:
        print("Choose an option: (1) Play/Pause (2) Next Track (3) Previous Track (q to quit)")
        choice = input("Enter choice: ")

        if choice == '1':
            play_pause()
        elif choice == '2':
            next_track()
        elif choice == '3':
            previous_track()
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
        time.sleep(1)
