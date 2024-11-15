"""
Задача 3
Напишите функции-генераторы, которые выводят элементы разложения sin,
cos и exp в ряды Тейлора. После, используя функциональный подход,
найдите сумму членов ряда и сравните её со значением вычисления функции из модуля math.
Выведите разницу в экспоненциальном представлении.

Разложение функций в ряд Тейлора:
"""

import math
from functools import reduce


def factorial(n):
    """
    Факториал числа n
    :param n: Целое число
    :return: 'аккумлятор' функци reduce
    """
    return reduce(lambda a, i: a * i, (x for x in range(n + 1) if x > 0), 1)


def exp(x, count=5):
    """
    Экспонента числа x
    :param x: Степень
    :param count: Колличество элементов ряда
    :return: 'аккумлятор' функци reduce
    """
    return reduce(lambda a, i: a + i, (((x ** n) / factorial(n)) for n in range(count)), 0)


def sin(x, count=5):
    """
    Синус
    :param x: Угол в радианах
    :param count: Колличество элементов ряда
    :return: 'аккумлятор' функци reduce
    """
    return reduce(lambda a, i: a + i,
                  ((((-1) ** n) * ((x ** (2 * n + 1)) / factorial(2 * n + 1))) for n in range(count)), 0)


def cos(x, count=5):
    """
    Косинус
    :param x: Угол в радианах
    :param count: Колличество элементов ряда
    :return: 'аккумлятор' функци reduce
    """
    return reduce(lambda a, i: a + i,
                  ((((-1) ** n) * ((x ** (2 * n)) / factorial(2 * n))) for n in range(count)), 0)


x = 1

print(f'{math.sin(x) - sin(x):.1e}')

print(f'{math.cos(x) - cos(x):.1e}')

print(f'{math.exp(x) - exp(x):.1e}')
