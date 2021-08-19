# Користувач вводить з клавіатури арифметичний вираз. Необхідно обчислити його значення з урахуванням пріоритетів
# введених математичних операцій і дужок. Якщо у виразі зустрічаються інші символи, видати повідомлення,
# що вираз введено некоректно.

arithmetical_expression = input('Print an arithmetical expression, please: ')

try:
    print(eval(arithmetical_expression))
except:
    print('The arithmetical expression was printed incorrect')
