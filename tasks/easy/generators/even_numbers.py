"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""


def get_even_number():
    a = range(2, 100, 2)
    for n in a:
        yield n
