"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list):
    list = []
    for n in some_list:
        if n not in list:
            list.append(n)
            print('No')
        else:
            print('Yes')
