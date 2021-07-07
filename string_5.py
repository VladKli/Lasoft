# Створити функцію для перевірки коректності розстановки дужок у виразі.

expression = input('Print an expression, please: ')


def check_brackets_for_correct_set(string):
    brackets_open = ('(', '[', '{')
    brackets_closed = (')', ']', '}')
    stack = []
    for bracket in string:
        if bracket in brackets_open:
            stack.append(bracket)
        if bracket in brackets_closed:
            if len(stack) == 0:
                return False
            index = brackets_closed.index(bracket)
            open_bracket = brackets_open[index]
            if stack[-1] == open_bracket:
                stack = stack[:-1]
            else:
                return False
    return not stack


print(check_brackets_for_correct_set(expression))
