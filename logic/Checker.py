class Checker:
    # Методы проверки для Влада. Пока как заглушки

    # Содержание ВКР
    def check_content_structure(self):
        return None  # Заглушка

    def check_navigation(self):
        return False  # Заглушка

    def check_headings(self):
        return True  # Заглушка

    def check_numbering(self):
        return False  # Заглушка

    # Структурные элементы
    def check_sections_and_subsections(self):
        return True  # Проверка разделов и подразделов

    def check_abbreviations_list(self):
        return True  # Проверка списка сокращений и условных обозначений

    def check_terms_list(self):
        return False  # Проверка списка терминов

    def check_introduction_and_conclusion(self):
        return True  # Проверка введения и заключения

    def check_sources_list(self):
        return False  # Проверка списка используемых источников

    def check_appendices(self):
        return True  # Проверка приложения

    # Визуальные элементы
    def check_illustrations(self):
        return True  # Проверка иллюстраций

    def check_equations(self):
        return False  # Проверка формул и уравнений

    def check_tables(self):
        return True  # Проверка таблиц

    # Стили
    def check_page_format(self):
        return True  # Проверка формата листа

    def check_margins(self):
        return True  # Проверка размеров полей

    def check_line_spacing(self):
        return False  # Проверка интервалов текста

    def check_font_style(self):
        return True  # Проверка шрифта
