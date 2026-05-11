import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
kivy.require('1.9.0')

class AnyStreak(App):
    def build(self):
        return AnchorLayout()
    

anystreak = AnyStreak()

anystreak.run()