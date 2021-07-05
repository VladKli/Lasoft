# Написати функцію, яка визначає чи є рядок паліндромом (тобто рядк, який можна читати зліва направо,
# і справа наліво: «А роза упала на лапу Азора», «Аргентина манит негра»).

palindrome = input('Print a palindrome, please: ')


def find_palindrome_string(string):
    string_without_spaces = ''.join(string.split()).lower()
    if string_without_spaces == string_without_spaces[::-1]:
        return 'The string is a palindrome'
    else:
        return 'The string is not a palindrome'


print(find_palindrome_string(palindrome))
