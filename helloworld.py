"""
Test app following tutorial: https://towardsdatascience.com/building-android-apps-with-python-part-1-603820bebde8
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class Main(App):
    def build(self):
        # return Label(text='hello world')
        return Button(text='Hello World',
                        size_hint=(0.5,0.5))


Main().run()