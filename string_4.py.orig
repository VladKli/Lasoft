# Створити функцію, що дозволяє вставляти (видаляти) стрічку в (з) масив (-а) стрічок.
# Вставляти та видаляти в ту/з тієї позицію (-ї) яку вкаже користувач

lis = ['Створити функцію', 'що дозволяє вставляти', 'видаляти стрічку', 'в масив', 'що дозволяє вставляти']

string = input('Print a string you want to add to the string\'s list, please: ')
index = int(input('Print new position of the string in the list. Reminder: the first element in lists start with 0. '))


def insert_string(position, insert):
    lis.insert(position, insert)
    return lis


def remove_string(position):
    lis.pop(position)
    return lis


print(insert_string(index, string))

index_1 = int(input('Print position of unnecessary element, please: '))

print(remove_string(index_1))
