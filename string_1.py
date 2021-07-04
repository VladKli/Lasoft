# Створити метод який приймає, введену користувачем стрічку і виводить на екран статистику по цій стрічці.
# Статистика повинна включати загальну кількість символів, кількість букв (і скільки букв в верхньому і нижньому
# регістрі, кількість цифр, символів пунктуації та кількість символів пробілів.

string = input('Print a string, please: ')


def make_statistic(text):

    letters_count = 0
    lower = 0
    upper = 0
    digits_count = 0
    punct = 0
    spaces = 0

    for letter in text:
        if letter.isalpha():
            letters_count += 1
            if letter.islower():
                lower += 1
            else:
                upper += 1
        elif letter.isdigit():
            digits_count += 1
        elif letter.isspace():
            spaces += 1
        else:
            punct += 1

    print(f'Amount of symbols: {len(string)}, amount of letters: {letters_count}, lower register: {lower},'
          f'upper register: {upper}, amount of digits: {digits_count}, punctuation symbols: {punct}, spaces: {spaces}')


make_statistic(string)

