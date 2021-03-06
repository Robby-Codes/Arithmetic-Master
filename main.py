from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen


class HomeScreen(Screen):
    pass


class AdditionScreen(Screen):
    pass


class SubtractionScreen(Screen):
    pass


class MultiplicationScreen(Screen):
    pass


class DivisionScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('gui.kv')

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')


class ArithmeticMasterApp(App):
    def build(self):
        self.title = 'Arithmetic Master'
        self.icon = 'icon.png'
        return kv


if __name__ == "__main__":
    ArithmeticMasterApp().run()
