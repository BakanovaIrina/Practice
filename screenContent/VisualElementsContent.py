from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from logic.Checker import Checker
from components.ResultTable import ResultTable

class VisualElementsContent(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'top'

        layout = BoxLayout(orientation='vertical', spacing=20,
                           size_hint=(None, None), pos_hint={'center_x': 0.5})
        layout.width = 600
        layout.height = 260

        layout.add_widget(Label(
            text="Визуальные элементы",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=50
        ))

        layout.add_widget(Label(
            text="Результаты проверки таблиц, иллюстраций и формул.",
            font_size=18,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=30
        ))

        checker = Checker()

        checks = {
            "Иллюстрации": checker.check_illustrations,
            "Формулы и уравнения": checker.check_equations,
            "Таблицы": checker.check_tables,
        }

        result_table = ResultTable(checks)
        layout.add_widget(result_table)

        self.add_widget(layout)