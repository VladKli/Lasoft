# Написати функцію, що перетворює дробове або ціле число в рядок.
# якщо вводити 1.3 результат текстом -> одна ціла три десятих

number = float(input('Print a number from 0 to 10, please: '))


def transform_to_words(num):
    integer_part = ['zero ', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ']

    units_part = str(num).split('.')[0]
    decimal_part = str(num).split('.')[1]

    if str(num - int(num))[-1] == '0':
        return integer_part[int(num)]

    elif (num >= 1) and (num < 20):
        transferred_num = integer_part[int(units_part)] + 'point ' + integer_part[int(decimal_part)]
        return transferred_num


try:
    print(transform_to_words(number))
except IndexError:
    print('A number should be in range from 0 to 10')
