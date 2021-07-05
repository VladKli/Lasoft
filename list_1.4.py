# В масиві, який складається із n чисел, обчислити:
# Кількість елементів, які розташовані між А і B,  де А, В – задаються користувачем.
# handle if a or b doesn't exists

li = [1, 2, 67, -3, 6, 0.25, -3.89, 4.52, -12, -7]

num_1 = float(input('Please, set a number which exist in the list: '))
num_2 = float(input('Please, set the second number: '))


def get_nums(lis, a, b):
    a_1 = lis.index(a)
    b_1 = lis.index(b)
    if a_1 < b_1:
        a_1 += 1
        l1 = lis[a_1: b_1]
        return len(l1)
    else:
        b_1 += 1
        l2 = lis[b_1: a_1]
        return len(l2)


try:
    print(get_nums(li, num_1, num_2))
except ValueError:
    print('Please, set 2 numbers which exist in the list')
