"""
Реализуйте «Шифр Цезаря»:

вводим с клавиатуры размер смещения, оно может быть отрицательным и положительным;
вводим с клавиатуры текст сообщения;
на экран выводится шифрованное сообщение и результат расшифровки.
"""



def shifr_Cezar(message:str, step_:int, type_message: bool = False) -> str:
    """
    Код "Цезаря"!
    :param message: текст сообщения
    :param step_: размер смещения
    :param type_message: True - расшифровка, False - шифрование
    :return: str 
    """
    alfavit_ru_up = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л',
                     'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    alfavit_ru_low = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л',
                      'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'б',
                      'я']
    alfavit_en_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
    alfavit_en_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't',
                      'u', 'v', 'w', 'x', 'y', 'z']

    # print(id(message))
    result = list(message)
    # print(id(result))
    if step_>0:
        col_vo_en = 0
        col_vo_ru = 0
        if(abs(step_) >= len(alfavit_en_low)):
            col_vo_en = ((abs(step_) // len(alfavit_en_low)) + 1) * len(alfavit_en_low)
        if (abs(step_) >= len(alfavit_ru_low)):
            col_vo_ru = ((abs(step_) // len(alfavit_ru_low)) + 1) * len(alfavit_ru_low)
        step_en = int((col_vo_en - abs(step_)) if col_vo_en != 0 else step_)
        step_ru = int((col_vo_ru - abs(step_)) if col_vo_ru != 0 else step_)
    elif step_<0:
        col_vo_en = 0
        col_vo_ru = 0
        if (abs(step_) >= len(alfavit_en_low)):
            col_vo_en = ((abs(step_) // len(alfavit_en_low)) + 1) * len(alfavit_en_low)
        if (abs(step_) >= len(alfavit_ru_low)):
            col_vo_ru = ((abs(step_) // len(alfavit_ru_low)) + 1) * len(alfavit_ru_low)
        step_en = int(-(col_vo_en - abs(step_)) if col_vo_en != 0 else step_)
        step_ru = int(-(col_vo_ru - abs(step_)) if col_vo_ru != 0 else step_)


    for ind, i in enumerate(result):
        if i.isalpha():
            if type_message:
                if i in alfavit_ru_low:
                    index_i = alfavit_ru_low.index(i)
                    index = (index_i - step_ru) if (index_i - step_ru) < len(alfavit_ru_low) else (
                            index_i - step_ru - len(alfavit_ru_low))
                    result[ind] = alfavit_ru_low[index]
                elif i in alfavit_ru_up:
                    index_i = alfavit_ru_up.index(i)
                    index = (index_i - step_ru) if (index_i - step_ru) < len(alfavit_ru_up) else (
                                index_i - step_ru - len(alfavit_ru_up))
                    result[ind] = alfavit_ru_up[index]
                elif i in alfavit_en_low:
                    index_i = alfavit_en_low.index(i)
                    index = (index_i - step_en) if (index_i - step_en) < len(alfavit_en_low) else (
                                index_i - step_en - len(alfavit_en_low))
                    result[ind] = alfavit_en_low[index]
                elif i in alfavit_en_up:
                    index_i = alfavit_en_up.index(i)
                    index = (index_i - step_en) if (index_i - step_en) < len(alfavit_en_up) else (
                            index_i - step_en - len(alfavit_en_up))
                    result[ind] = alfavit_en_up[index]
            else:
                if i in alfavit_ru_low:
                    index_i = alfavit_ru_low.index(i)
                    index = (index_i + step_ru) if (index_i + step_ru) < len(alfavit_ru_low) else (
                                index_i + step_ru - len(alfavit_ru_low))
                    result[ind] = alfavit_ru_low[index]
                elif i in alfavit_ru_up:
                    index_i = alfavit_ru_up.index(i)
                    index = (index_i + step_ru) if (index_i + step_ru) < len(alfavit_ru_up) else (
                                index_i + step_ru - len(alfavit_ru_up))
                    result[ind] = alfavit_ru_up[index]
                elif i in alfavit_en_low:
                    index_i = alfavit_en_low.index(i)
                    index = (index_i + step_en) if (index_i + step_en) < len(alfavit_en_low) else (
                                index_i + step_en - len(alfavit_en_low))
                    result[ind] = alfavit_en_low[index]
                elif i in alfavit_en_up:
                    index_i = alfavit_en_up.index(i)
                    index = (index_i + step_en) if (index_i + step_en) < len(alfavit_en_up) else (
                            index_i + step_en - len(alfavit_en_up))
                    result[ind] = alfavit_en_up[index]

    return ''.join(result)


if __name__ == '__main__':
    print(f'Шифрованное сообщение: {shifr_Cezar("Как дела, Петя?", 9)}')
    print('Расшифрованное сообщение: "Как дела, Петя?"')

    print('_______________________________________')

    print(f'Шифрованное сообщение: {shifr_Cezar("Привет, мир!", 31)}')
    print('Расшифрованное сообщение: "Привет, мир!"')

    print('_______________________________________')

    print(f'Расшифрованное сообщение: {shifr_Cezar(shifr_Cezar("Как дела, Петя?", 9), 9, True)}')
    print(f'Шифрованное сообщение: "{shifr_Cezar("Как дела, Петя?", 9)}"')

    print('_______________________________________')

    print(f'Расшифрованное сообщение: {shifr_Cezar(shifr_Cezar("Привет, мир!", 31), 31, True)}')
    print(f'Шифрованное сообщение: "{shifr_Cezar("Привет, мир!", 31)}"')
