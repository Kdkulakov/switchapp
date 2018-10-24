
import requests

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class SwitchApp(App):

    def switchoff(self, *args, **kwargs):
        url = 'http://192.168.1.150/?R7_off'
        try:
            req = requests.get(url)
        except ConnectionError:
            pass
        return req

    def switchon(self, *args, **kwargs):
        url = 'http://192.168.1.150/?R7_on'
        try:
            req = requests.post(url)
        except ConnectionError:
            pass
        return req

    def build(self):
        boxl = BoxLayout(
            spacing=20
        )

        boxl.add_widget(Button(
            text="ON",
            on_release=self.switchon,
            font_size=40,
            color=[.37, .52, .84, .7],
            background_color=[.37, .52, .84, .7]
        ))

        boxl.add_widget(Button(
            text="OFF",
            on_release=self.switchoff,
            color=[.37, .52, .84, .7],
            font_size=40,
            background_color=[.37, .52, .84, .7]

        ))

        return boxl



if __name__ == "__main__":
    SwitchApp().run()