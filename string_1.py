# Створити метод який приймає, введену користувачем стрічку і виводить на екран статистику по цій стрічці.
# Статистика повинна включати загальну кількість символів, кількість букв (і скільки букв в верхньому і нижньому
# регістрі, кількість цифр, символів пунктуації та кількість символів пробілів.

string = input('Print a string, please: ')


def make_statistic(text):
    letters_count = 0
    lower_letters_count = 0
    upper_letters_count = 0
    digits_letters_count = 0
    symbol_letters_count = 0
    spaces_letters_count = 0

    for letter in text:
        if letter.isalpha():
            letters_count += 1
            if letter.islower():
                lower_letters_count += 1
            else:
                upper_letters_count += 1
        elif letter.isdigit():
            digits_letters_count += 1
        elif letter.isspace():
            spaces_letters_count += 1
        else:
            symbol_letters_count += 1

    return {'total number of characters': len(string),
            'amount of letters': letters_count,
            'amount of letter in lower case': lower_letters_count,
            'amount of letter in upper case': upper_letters_count,
            'amount of digits': digits_letters_count,
            'amount of symbols': symbol_letters_count,
            'amount of spaces': spaces_letters_count}


print(make_statistic(string))

