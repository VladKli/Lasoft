# Створити функцію, що дозволяє вставляти (видаляти) стрічку в (з) масив (-а) стрічок.

lis = ['Створити функцію', 'що дозволяє вставляти', 'видаляти стрічку', 'в масив']


def change_list(paste, delete):

    lis.append(paste)
    lis.remove(delete)
    return lis


print(change_list('new string'))
