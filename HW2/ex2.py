"""
Задача 2
Напишите функцию-генератор, которая возвращает очередной элемент,
содержащий числа Фибоначчи в количестве, переданном в функцию.
Если число не передано, то мы возвращаем бесконечную последовательность.
Ограничьте искусственно вывод 100 элементов.
"""

def get_fib_numbers(qty = 100):
    """

    :param qty: кол-во элементов
    :yield: генератор
    """
    a, b = 0, 1
    for _ in range(qty):
        yield a
        a, b = b, a + b

fib_numbers = list(get_fib_numbers(10))
try:
    assert len(fib_numbers) == 10, "Ошибка!"
    print(fib_numbers)
except AssertionError as ex:
    print(ex)
