# Дано два масиви : А[n] и B[m]. Необхідно створити третій масив, в якому потрібно зібрати:
# Знайти суму всіх від’ємних елементів масиву А,яких немає в масиві В і які не повторюються в масиві А.

A = [1, -0.25, 1, -7, -7, -2, 555, -6, -6, -6]
B = [1, 7, 6, 1, 33, -29, -0.25, -2]


def make_list(li_1):
    lis = []
    for el in li_1:
        if li_1.count(el) < 2:
            lis.append(el)
    return lis


new_list = make_list(A)

result = [num for num in new_list if (num < 0) and (num not in B)]
print(sum(result))
