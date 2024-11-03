import speech_recognition as sr
import pyttsx3
import schedule
import time
from datetime import datetime, timedelta

# Initialize text-to-speech engine
engine = pyttsx3.init()

# To-do list
todo_list = []


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the service.")
            return ""


def add_task_to_list():
    speak("What task would you like to add to your to-do list?")
    task = listen()
    if task:
        speak(
            "When is the deadline for this task? Please say 'today', '1 day after today', '2 days after today', and so on.")
        deadline_str = listen()

        days_after = 0
        if 'today' in deadline_str:
            days_after = 0
        else:
            try:
                days_after = int(deadline_str.split()[0])
            except ValueError:
                speak("I couldn't understand the number of days. Please try again.")
                return

        deadline = datetime.now() + timedelta(days=days_after)

        speak("How important is this task? Please say a number between 1 and 5.")
        importance = listen()

        speak("What is the priority of this task? Please say a number between 1 and 5.")
        priority = listen()

        speak("Is this task repeated? Please say 'yes' or 'no'.")
        repeated = listen()

        repeat_frequency = None
        if repeated == 'yes':
            speak("How often would you like to repeat it? For example, daily, weekly, monthly.")
            repeat_frequency = listen()

        task_info = {
            'task': task,
            'deadline': deadline,
            'importance': int(importance),
            'priority': int(priority),
            'repeated': repeated,
            'repeat_frequency': repeat_frequency
        }

        todo_list.append(task_info)
        speak(f"Task '{task}' has been added to your to-do list.")

        set_reminder(task_info)


def set_reminder(task_info):
    task = task_info['task']
    deadline = task_info['deadline']
    repeat_frequency = task_info['repeat_frequency']

    def reminder():
        speak(f"Reminder: You have a task '{task}' due on {deadline.strftime('%Y-%m-%d')}.")

    # Set initial reminder
    schedule.every().day.at(deadline.strftime("%H:%M")).do(reminder)

    # Set repeated reminders if necessary
    if task_info['repeated'] == 'yes':
        if repeat_frequency == 'daily':
            schedule.every().day.at(deadline.strftime("%H:%M")).do(reminder)
        elif repeat_frequency == 'weekly':
            schedule.every().week.at(deadline.strftime("%H:%M")).do(reminder)
        elif repeat_frequency == 'monthly':
            schedule.every().month.at(deadline.strftime("%H:%M")).do(reminder)


if __name__ == "__main__":
    speak("Voice assistant started. How can I assist you today?")

    while True:
        command = listen()
        if 'create task list' in command:
            add_task_to_list()
        elif 'exit' in command:
            speak("Goodbye!")
            break

        schedule.run_pending()
        time.sleep(1)
