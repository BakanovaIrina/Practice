from kivy.uix.screenmanager import Screen

from screenContent.MainScreenContent import MainScreenContent

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(MainScreenContent())

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size
