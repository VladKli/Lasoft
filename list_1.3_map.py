# В масиві, який складається із n чисел, обчислити : Кількість елементів масиву, менших С (С – задається користувачем);
# use map

lis = [1, 2, 67, -3, 6, 0.25, -3.89, 4.52, -12, -7]

nums = float(input('Set a digit: '))


def calculate(c):
    if c < nums:
        return 1


amount = list(map(calculate, lis))
count = amount.count(1)

print(count)
