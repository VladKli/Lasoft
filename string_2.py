# Користувач вводить рядок і символ. У рядку знайти всі входження цього символу і перевести його в верхній регістр,
# а також видалити частину рядка, починаючи з останнього входження цього символу і до кінця.

string = input('Print a string, please: ')
symbol = input('Print a symbol, please: ')


def change_to_upper_case_by_symbol(string, symb):
    new_str = string.replace(symb, symb.upper())
    return new_str


def remove_by_last_symbol(string, symb):
    index = string.rfind(symb)
    result = string[0:index]
    return result


print(change_to_upper_case_by_symbol(string, symbol))
print(remove_by_last_symbol(string, symbol))
