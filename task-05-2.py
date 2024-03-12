'''
Необхідно створити функцію generator_numbers, яка буде аналізувати текст, 
ідентифікувати всі дійсні числа, що вважаються частинами доходів, і повертати 
їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами 
з обох боків. Також потрібно реалізувати функцію sum_profit, яка буде використовувати 
generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

Вимоги до завдання:
- Функція generator_numbers(text: str) повинна приймати рядок як аргумент і 
  повертати генератор, що ітерує по всіх дійсних числах у тексті. Дійсні числа у 
  тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
- Функція sum_profit(text: str, func: Callable) має використовувати генератор 
  generator_numbers для обчислення загальної суми чисел у вхідному рядку 
  та приймати його як аргумент при виклику.
'''
from typing import Callable

import re

def generator_numbers(text: str) -> list:
    # RE to search:
    #  sign
    #  any digits (\d*) until DOT
    #  DOT (\.)
    #  one (\d) or two (|\d) digits arter DOT
    new_text = re.findall(r"[-+]?\d*\.\d+|\d+", text)
    for digit_in_text in new_text:
        yield float(digit_in_text)

def sum_profit(text: str, func: Callable[[str], list]) -> float:
    # Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків
    return sum(generator_numbers(text))

'''
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
'''
