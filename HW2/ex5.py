"""
Вам дан список молекул и их атомная масса:

H (водород) — 1.008
O (кислород) — 15.999;
S (сера) — 32.066;
Na (натрий) — 22.990;
Cl (хлор) — 35.453;
K (калий) — 39.098.
Посчитайте молярную массу молекул, используя методы функционального программирования.
Выведите значения в порядке возрастания молярной массы.
"""
from functools import reduce


def foo(*args):
    """

    :param args:
    :return:
    """
    print("id - Параметр:", id(args))
    args = list(args)
    print("id - Аргумент:", id(args))
    for i in range(len(args)):
        assert isinstance(args[i], str), "Аргументы должныбыть типа - 'str'"
        args[i] = args[i].upper()
        args[i] = args[i].strip()
        args[i] = args[i].split('-')
        temp_result = []
        for j in range(len(args[i])):
            # Два символа в наимновании элемента
            args[i][j] = args[i][j].replace('NA', ' 22.990 ')
            args[i][j] = args[i][j].replace('CL', ' 35.453 ')
            # Один символ в наимновании элемента
            args[i][j] = args[i][j].replace('H', ' 1.008 ')
            args[i][j] = args[i][j].replace('O', ' 15.999 ')
            args[i][j] = args[i][j].replace('S', ' 32.066 ')
            args[i][j] = args[i][j].replace('K', ' 39.098 ')
            args[i][j] = args[i][j].strip()
            try:
                temp = [float(x) for x in args[i][j].split(' ') if x]
                if len(temp):
                    temp_result.append(reduce(lambda a, x: a * x, temp, 1))
                else:
                    temp_result.append(0)
            except Exception:
                temp_result = "Нет таких элементов в списке!"
                break
        args[i] = temp_result if isinstance(temp_result, str) else sum(temp_result)

    return args


arr = ['H2-O', 'Na-Cl', 'H-CL', 'K-CL', 'H2-S-O4', 'Si']

try:
    res = foo(*arr)

    for i, el in enumerate(arr):
        if isinstance(res[i], float):
            print(f'{el}\t{res[i]:.3f}')
        else:
            print(f'{el}\t{res[i]}')

except AssertionError as ex:
    print(ex)


