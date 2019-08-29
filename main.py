from kivy.app import App
from kivy.lang import Builder
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


class ArithmeticMasterApp(App):
    def build(self):
        self.title = 'Arithmetic Master'
        return kv


if __name__ == "__main__":
    ArithmeticMasterApp().run()
