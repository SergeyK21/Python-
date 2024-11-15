"""
Расширим возможности калькулятора, который вы делали в первом модуле,
и модифицируем логику обработки выражений. Теперь будем собирать возникающие исключения
с помощью системы логирования.

Калькулятор должен поддерживать четыре операции: сложение (+), умножение (×),
вычитание (−), деление (÷), определённые с целыми числами и числами с плавающей точкой,
а также должен быть толерантен к пробелам, то есть между операндами и числами может
быть неограниченное число пробелов.

Для обработки выражений реализуйте функциональный подход: создайте функцию
для каждой операции и используйте её как объект.
"""

import logging

logger1 = logging.getLogger('Calculate')
logger1.setLevel(logging.INFO)

logger2 = logging.getLogger('ERROR')
logger2.setLevel(logging.DEBUG)

ch = logging.FileHandler(
    filename="results.txt",
    mode='w',
    encoding='utf-8'
)
ch.setLevel(logging.INFO)

fh = logging.FileHandler(
    filename="logs.log",
    mode='w',
    encoding='utf-8'
)
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger1.addHandler(ch)
logger2.addHandler(fh)


def operation(temp_str):
    """

    :param temp_str: Строка выражения
    :return: float(Результат выражения)
    """
    temp_str = temp_str.replace(' ', '')
    temp_str = temp_str.replace('\n', '')
    temp_str = temp_str.replace('\t', '')
    temp_str = temp_str.replace(',', '.')
    if temp_str.count("+") > 0:
        temp_str = temp_str.split(sep="+")
        temp_digit = []
        for el in temp_str:
            temp_digit.append(float(el))
        return temp_digit[0] + temp_digit[1]
    elif temp_str.count("-"):
        temp_str = temp_str.split(sep="-")
        temp_digit = []
        for el in temp_str:
            temp_digit.append(float(el))
        return temp_digit[0] - temp_digit[1]

    elif temp_str.count("*"):
        temp_str = temp_str.split(sep="*")
        temp_digit = []
        for el in temp_str:
            temp_digit.append(float(el))
        return temp_digit[0] * temp_digit[1]

    elif temp_str.count("/"):
        temp_str = temp_str.split(sep="/")
        temp_digit = []
        for el in temp_str:
            temp_digit.append(float(el))
        return temp_digit[0] / temp_digit[1]
    else:
        raise Exception("В вырвжении нет опператора")


with open('calc.txt', 'w', encoding='utf-8') as file:
    file.write("3,1  +    d\n")
    file.write("  4,3 + 5  \n")
    file.write("  4 - 5  \n")
    file.write("  4 * 5  \n")
    file.write("  20 / 5  \n")
    file.write("  21 / 5  \n")
    file.write("  21 / 0  \n")

with open('calc.txt', 'r', encoding='utf-8') as file:
    list_str = file.readlines()

for i, el in enumerate(list_str):
    try:
        str_el = el.replace('\n', '')
        logger1.info(f"Строка № {i+1} - {str_el} = {operation(el)}")
    except Exception as ex:
        logger2.debug(f"Строка № {i+1} - {str(ex)}")

