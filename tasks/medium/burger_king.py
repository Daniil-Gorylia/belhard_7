"""
С помощью декораторов реализовать конвейер сборки бургера

Написать декоратор bread, который:
 - до декорируемой функции будет печатать "</------------\\>"
 - после декорируемой функции будет печатать "<\\____________/>"


Написать декоратор tomato, который:
 - до декорируемой функции будет печатать "*** помидоры ****"

Написать декоратор salad, который:
 - до декорируемой функции будет печатать "~~~~ салат ~~~~~"

Написать декоратор cheese, который:
 - до декорируемой функции будет печатать "^^^^^ сыр ^^^^^^"

Написать декоратор onion, который:
 - до декорируемой функции будет печатать "----- лук ------"

Написать функцию beef, которая:
 - печатает "### говядина ###"

Написать функцию chicken, которая:
 - печатает "|||| курица ||||"

1) Собрать с помощью декораторов гамбургер:
    - булка
    - лук
    - помидоры
    - говядина
    - булка

2) Собрать с помощью декораторов чикенбургер:
    - булка
    - сыр
    - салат
    - курица
    - булка
"""


def bread(func):
    def start_func():
        print('</------------\\>')
        if func() is not None:
            print(func())
        print('<\\____________/>')
    return start_func


def onion(func):
    def start_func():
        print('----- лук ------')
        if func() is not None:
            print(func())
    return start_func


def tomato(func):
    def start_func():
        print('*** помидоры ****')
        if func() is not None:
            print(func())
    return start_func


def salad(func):
    def start_func():
        print('~~~~ салат ~~~~~')
        if func() is not None:
            print(func())
    return start_func


def cheese(func):
    def start_func():
        print('^^^^^ сыр ^^^^^^')
        if func() is not None:
            print(func())
    return start_func


@bread
@onion
@tomato
def beef():
    a = '### говядина ###'
    return a


@bread
@cheese
@salad
def chicken():
    a = '|||| курица ||||'
    return a
