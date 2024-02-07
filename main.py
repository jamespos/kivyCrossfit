from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from warmup_workout_file import warmup_workout_data
from main_workout_file import main_workout_data
import random


class MainApp(MDApp):
    text = StringProperty()
    textField = StringProperty()

    def home_screen(self):
        self.root.ids.screen_manager.current = "main"

    def warm_up(self):
        self.root.ids.screen_manager.current = "warmup"

    def get_warmup(self):
        warmup_workout_bank = []
        for x in warmup_workout_data:
            ex_value = x['exercise']
            warmup_workout_bank.append(ex_value)
        current_workout_warmup = random.choice(warmup_workout_bank)
        print(current_workout_warmup)
        self.root.ids.textField2.text = current_workout_warmup

    def reset_warmup(self):
        self.root.ids.textField2.add_widget(
            Label(
                text="",
                halign='center',
                pos_hint={"center_x": 0.5, "center_y": .6},
            )
        )
        self.get_warmup()

    def main_workout(self):
        self.root.ids.screen_manager.current = "mainWorkout"

    def get_main_workout(self):
        main_workout_bank = []
        for x in main_workout_data:
            ex_value = x['exercise']
            main_workout_bank.append(ex_value)
        current_workout_main = random.choice(main_workout_bank)
        print(current_workout_main)
        self.root.ids.textField1.text = current_workout_main

    def reset_main(self):
        self.root.ids.textField1.add_widget(
            Label(
                text="",
                halign='center',
                pos_hint={"center_x": 0.5, "center_y": .6},
            )
        )
        self.get_main_workout()

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.title = "Cossfit"
        self.icon = 'data/dumbell.png'

        return Builder.load_file('main.kv')


if __name__ == "__main__":
    app = MainApp()
    app.run()
