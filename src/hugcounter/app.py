"""
A counter of hugs for my love
"""

import os
import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class HugCounter(toga.App):
    def __init__(self, *args, **kwargs):
        self.counter_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'counter.txt')
        super().__init__(*args, **kwargs)


    def startup(self):
        self.main_box = toga.Box(style=Pack(direction=COLUMN, padding=10, alignment='center'))

        self.counter_input = toga.TextInput(style=Pack(font_size=40, padding=5, width=200))
        self.main_box.add(self.counter_input)

        self.increment_button = toga.Button("Increment", on_press=self.increment_counter, style=Pack(padding=5))
        self.main_box.add(self.increment_button)

        self.increment_button = toga.Button("Increment by 10", on_press=self.increment_counter_10, style=Pack(padding=5))
        self.main_box.add(self.increment_button)

        self.set_button = toga.Button("Set Number", on_press=self.set_number_from_input, style=Pack(padding=5))
        self.main_box.add(self.set_button)

        self.set_button = toga.Button("Clear", on_press=self.number_clear, style=Pack(padding=5))
        self.main_box.add(self.set_button)

        self.load_counter()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = self.main_box
        self.main_window.show()

    def increment_counter(self, widget):
        try:
            current_value = int(self.counter_input.value)
            new_value = current_value + 1
            self.counter_input.value = str(new_value)
            self.save_counter()
        except ValueError:
            self.counter_input.value = "Invalid Input"

    def increment_counter_10(self, widget):
        try:
            current_value = int(self.counter_input.value)
            new_value = current_value + 10
            self.counter_input.value = str(new_value)
            self.save_counter()
        except ValueError:
            self.counter_input.value = "Invalid Input"

    def set_number_from_input(self, widget):
        try:
            new_value = int(self.counter_input.value)
            self.counter_input.value = str(new_value)
            self.save_counter()
        except ValueError:
            self.counter_input.value = "Invalid Input"

    def number_clear(self, widget):
        try:
            self.counter_input.value = str(0)
            self.save_counter()
        except ValueError:
            self.counter_input.value = "Invalid Input"

    def load_counter(self):
        print(f"Loading counter from: {self.counter_file}")
        if os.path.exists(self.counter_file):
            with open(self.counter_file, 'r') as file:
                try:
                    value = file.read().strip()
                    if value.isdigit():
                        self.counter_input.value = value
                except:
                    self.counter_input.value = "0"
        else:
            # 文件不存在时初始化为 0
            self.counter_input.value = "0"

    def save_counter(self):
        with open(self.counter_file, 'w') as file:
            file.write(self.counter_input.value)

def main():
    return HugCounter("HugCounter", "org.beeware.hugcounter")
