from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

from logic.Checker import Checker
from components.ResultTable import ResultTable

class StylesContent(AnchorLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'top'

        layout = BoxLayout(orientation='vertical', spacing=20,
                           size_hint=(None, None), pos_hint={'center_x': 0.5})
        layout.width = 600
        layout.height = 330

        layout.add_widget(Label(
            text="Стили",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=50
        ))

        layout.add_widget(Label(
            text="Результаты проверки стилей шаблона, включая шрифт, \nлист, поля и интервалы.",
            font_size=18,
            color=(0, 0, 0, 1),
            size_hint=(1, None),
            height=60,
            line_height=1.5,
            padding=60,
            halign='left',
            valign='middle',
            text_size=(600, None),
        ))

        checker = Checker()

        checks = {
            "Формат листа": checker.check_page_format,
            "Размеры полей": checker.check_margins,
            "Интервалы текста": checker.check_line_spacing,
            "Шрифт": checker.check_font_style,
        }

        result_table = ResultTable(checks)
        layout.add_widget(result_table)

        self.add_widget(layout)