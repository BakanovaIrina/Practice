from kivy.uix.screenmanager import Screen

from screenContent.StylesContent import StylesContent

class StylesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        self.add_widget(StylesContent())

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size