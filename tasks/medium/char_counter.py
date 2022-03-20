"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""
STR_VAL = 'python is the fastest-growing major programming language'


def count_char(str_val):
    count = {}
    for s in str_val:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    for key in count:
        if count[key] > 1:
            return count
