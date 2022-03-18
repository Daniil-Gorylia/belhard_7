"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:

    def __init__(self, brand='Apple', model='Iphone SE 2020', issue_year=2020):
        self.caller = None
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name='Alex'):
        self.caller = name
        return f"Звонит {self.caller}"

    def get_info(self):
        get_info = (self.brand, self.model, self.issue_year)
        return get_info
