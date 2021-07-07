# Написати функцію, що перетворює рядок в дробове або ціле число.

string = input('Enter an writing equivalent of number, please: ')


def transform_to_number(text):
    units_part = {'zero': 0,
                  'one': 1,
                  'two': 2,
                  'three': 3,
                  'four': 4,
                  'five': 5,
                  'six': 6,
                  'seven': 7,
                  'eight': 8,
                  'nine': 9,
                  'ten': 10,
                  }

    if text in units_part:
        return units_part[text]
    elif text not in units_part:
        integer_part = text.split(' ')[0]
        decimal_part = text.split(' ')[-1]
        return float(str(units_part[integer_part]) + '.' + str(units_part[decimal_part]))


print(transform_to_number(string))
