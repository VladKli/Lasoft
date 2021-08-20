# Користувач вводить рядок і символ. У рядку знайти всі входження цього символу і перевести його в верхній регістр,
# а також видалити частину рядка, починаючи з останнього входження цього символу і до кінця.

string = input('Print a string, please: ')
symbol = input('Print a symbol, please: ')


def find_result(text, symb):
    new_str = ''
    result = ''
    for el in text:
        if el == symb:
            new_str = text.replace(el, symb.upper())
    index = new_str.rfind(symb.upper())
    result = new_str[0:index]
    return result


print(find_result(string, symbol))
