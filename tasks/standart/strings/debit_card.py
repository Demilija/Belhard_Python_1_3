"""
Написать функцию hide_debit_numbers которая скрывает номер платежной карты,
оставляя только первые 4 и последние 4 цифра, а остальные заменяет символом *

Пример:
1111222233334444 -> 1111********4444
"""


def hide_debit_numbers(card_number: str) -> str:
    """Скрывает номер карты, оставляя толdько первые и последние 4 цифры

    :param card_number: номер карты 16 цифр
    :return: номер карты, вида 1111********1111
    """

    list_index = [4, 5, 6, 7, 8, 9, 10, 11]
    new = "*"
    for i in list_index:
        card_number = card_number[:i] + new + card_number[i + 1:]
    return card_number


if __name__ == '__main__':
    c_numb = input("Введите номер карты 16 цифр: ")
    if len(c_numb) != 16 or not c_numb.isdigit():
        raise ValueError("Некорректный номер карты")
    print(hide_debit_numbers(c_numb))
