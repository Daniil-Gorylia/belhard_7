"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""

def check_number(a):
    while a != 1 and a / 2 != 1:
        a = a - (a / 2)
        if a == int(a):
            continue
        elif a != int(a):
            return False
    if a / 2 == 1 or a == 1:
        return True

