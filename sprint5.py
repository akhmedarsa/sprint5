"""
ID 116559040
Модуль для расшифровки сжатых инструкций для марсохода.

Этот модуль включает функцию для расшифровки строки, содержащей
сжатые инструкции. Число перед квадратными скобками обозначает,
сколько раз надо повторить последовательность внутри скобок. Скобки
могут быть и вложенными.

Функции:
- decode_instructions(coded_string: str) -> str:
  расшифровывает сжатую строку инструкций.

Пример использования:
coded_string = '3[с]2[в]ш'
print(decode_instructions(coded_string))  # Вывод: 'сссввш'
"""


def decode_instructions(coded_string: str) -> str:
    """
    Расшифровывает сжатую строку инструкций.

    Аргументы:
    coded_string (str): Сжатая строка инструкций.

    Возвращает:
    str: Полная строка инструкций.
    """
    stack: list[tuple[str, str]] = []  # Стек для хранения строк и чисел
    current_num: str = ''  # Текущее число повторений
    current_string: str = ''  # Текущая расшифрованная строка

    for char in coded_string:
        if '0' <= char <= '9':
            # Строим число, если текущий символ - цифра
            current_num += char
        elif char == '[':
            # Сохраняем текущую строку и число в стек и обнуляем их
            stack.append((current_string, current_num))
            current_string = ''
            current_num = ''
        elif char == ']':
            # Извлекаем строку и число из стека, повторяем текущую строку
            prev_string, num = stack.pop()
            current_string = prev_string + int(num) * current_string
        else:
            # Добавляем текущий символ к строке, если это буква
            current_string += char

    return current_string


if __name__ == '__main__':
    coded_string = input()
    print(decode_instructions(coded_string))
