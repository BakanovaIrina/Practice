from kivy.uix.screenmanager import Screen

from screenContent.VisualElementsContent import VisualElementsContent

class VisualElementsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        self.add_widget(VisualElementsContent())

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size