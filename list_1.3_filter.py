# В масиві, який складається із n чисел, обчислити : Кількість елементів масиву, менших С (С – задається користувачем);
# use filter

lis = [1, 2, 67, -3, 6, 0.25, -3.89, 4.52, -12, -7]

nums = float(input('Set a digit: '))


def calculate(C):
    if C < nums:
        return C


amount = list(filter(calculate, lis))
print(len(amount))