"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value: int

    def __init__(self, value=0):
        self.value = value

    def increase(self, num=1):
        increase_value = self.value
        increase_value += num
        return increase_value

    def decrease(self, num=1):
        decrease_value = self.value
        decrease_value += num
        return decrease_value

    def __iter__(self):
        return self

    def __next__(self):
        num = self.value
        self.value += 1
        return num
