from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from logic.Checker import Checker
from components.ResultTable import ResultTable

class ContentWKR(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'top'

        layout = BoxLayout(orientation='vertical', spacing=20,
                           size_hint=(None, None))
        layout.width = 600
        layout.height = 300

        layout.add_widget(Label(
            text="Содержание ВКР",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=50
        ))

        layout.add_widget(Label(
            text="Результаты проверки содержания и навигации по шаблону ВКР.",
            font_size=18,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=30
        ))

        checker = Checker()

        checks = {
            "Состав содержания": checker.check_content_structure,
            "Навигация": checker.check_navigation,
            "Заголовки": checker.check_headings,
            "Нумерация": checker.check_numbering
        }

        result_table = ResultTable(checks)
        layout.add_widget(result_table)
        self.add_widget(layout)