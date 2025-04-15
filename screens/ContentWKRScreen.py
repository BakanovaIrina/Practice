from kivy.uix.screenmanager import Screen

from screenContent.ContentWKR import ContentWKR

class ContentWKRScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'

        self.add_widget(ContentWKR())

    def update_bg(self, *args):
        self.bg.pos = self.pos
        self.bg.size = self.size