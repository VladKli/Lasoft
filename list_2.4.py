# Дано два масиви : А[n] и B[m]. Необхідно створити третій масив, в якому потрібно зібрати:
# Елементи масиву B, які не включаються в A.

A = [1, -0.25, 1, 'abs', 555, 7, 6, 2, 0]
B = ['abs', 1, 7, 6, 1, 33, -29]

new_list = [num for num in B if num not in A]

print(new_list)