from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.textinput import TextInput
import requests


class MainMenu(BoxLayout):

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        # List of applications to launch
        self.applications = {
            "Brave": "brave",
            "Calculator": "calculator",
            "Camera": "camera",
        }

        # Left side: Music controls
        music_controls = BoxLayout(orientation='vertical', size_hint=(0.4, 1))
        self.play_button = Button(text="Play")
        self.pause_button = Button(text="Pause")
        self.stop_button = Button(text="Stop")

        # Bind buttons to placeholder functions
        self.play_button.bind(on_press=self.play_music)
        self.pause_button.bind(on_press=self.pause_music)
        self.stop_button.bind(on_press=self.stop_music)

        # Add buttons to the music control layout
        music_controls.add_widget(Label(text="Music Player Controls", font_size=18))
        music_controls.add_widget(self.play_button)
        music_controls.add_widget(self.pause_button)
        music_controls.add_widget(self.stop_button)

        # Center: Time display (shown when idle)
        self.time_label = Label(font_size=32)
        Clock.schedule_interval(self.update_time, 1)  # Update every second

        # Right side: App launcher and assistant
        right_controls = BoxLayout(orientation='vertical', size_hint=(0.4, 1))

        # Create buttons for existing applications
        for app_name, _ in self.applications.items():
            app_button = Button(text=app_name)
            app_button.bind(on_press=lambda x, name=app_name: self.launch_application(name))
            right_controls.add_widget(app_button)

        # Add input for new application names
        self.new_app_input = TextInput(hint_text='Enter new app name', multiline=False)
        add_app_button = Button(text="Add Application")
        add_app_button.bind(on_press=self.add_application)

        right_controls.add_widget(self.new_app_input)
        right_controls.add_widget(add_app_button)

        right_controls.add_widget(Label(text="Assistant Chat", font_size=18))
        assistant_button = Button(text="Chat with Assistant", background_color=(0, 1, 0, 1))
        assistant_button.bind(on_press=self.open_assistant_chat)
        right_controls.add_widget(assistant_button)

        # Add all layouts to the main layout
        self.add_widget(music_controls)
        self.add_widget(self.time_label)
        self.add_widget(right_controls)

    def play_music(self, instance):
        print("Play music")

    def pause_music(self, instance):
        print("Pause music")

    def stop_music(self, instance):
        print("Stop music")

    def update_time(self, dt):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.text = current_time

    def launch_application(self, app_name):
        url = f'http://192.168.183.239:5000/launch/{self.applications[app_name]}'
        try:
            response = requests.get(url)
            print(response.text)  # Log server response
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {e}")

    def add_application(self, instance):
        app_name = self.new_app_input.text.strip()
        if app_name:
            self.applications[app_name] = app_name.lower()  # Use the same name for the launch request
            self.new_app_input.text = ""  # Clear input field
            self.update_application_buttons()

    def update_application_buttons(self):
        self.clear_widgets()
        self.__init__()

    def open_assistant_chat(self, instance):
        print("Opening assistant chat")


class MainApp(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    MainApp().run()
