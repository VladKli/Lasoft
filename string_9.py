# З клавіатури вводиться ціле число в діапазоні від 0 до 1000000. Необхідно вивести його прописний стрічковий еквівалент

# The first option
# _____________________________________________________
# from num2words import num2words

# number = input('Print any number, please: ')

# print(num2words(0))
# _____________________________________________________


# The second option
number_1 = int(input('Print a number from 0 to 1000000, please: '))


def convert(num):
    units = ['', 'one ', 'two ', 'three ', 'four ', 'five ', 'six ', 'seven ', 'eight ', 'nine ', 'ten ', 'eleven ',
             'twelve ', 'thirteen ', 'fourteen ', 'fifteen ', 'sixteen ', 'seventeen ', 'eighteen ', 'nineteen ']

    tens = ['', '', 'twenty ', 'thirty ', 'forty ', 'fifty ', 'sixty ', 'seventy ', 'eighty ', 'ninety ']

    if (num >= 0) and (num < 20):
        return units[num]

    elif (num >= 20) and (num < 100):
        return tens[num // 10] + units[int(num % 10)]

    elif (num >= 100) and (num < 1000):
        return units[num // 100] + 'hundred ' + convert(int(num % 100))

    elif (num >= 1000) and (num < 10000):
        return units[num // 1000] + "thousand " + convert(int(num % 1000))

    elif (num >= 10000) and (num < 1000000):
        return convert(num // 1000) + "thousand " + convert(int(num % 1000))

    elif num == 1000000:
        return 'a million'


print(convert(number_1))
