# Дано два масиви : А[n] и B[m]. Необхідно створити третій масив, в якому потрібно зібрати:
# Елементи обох масивів.

A = [1, -0.25, 'abs', 555, 7]
B = ['abs', 1, 7, 6, 33, -29]

lis = []
lis.extend(A)
lis.extend(B)

# C = A + B

print(lis)
# print(C)