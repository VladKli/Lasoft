# Кожен студент характеризується такими атрибутами : прізвище, імя, по  батькові, номер студентського квитка,
# рік народження, місце народження, адреса, стать, сімейний стан, стипендія, кімната в гуртожитку.
# В одній кімнати проживає до трьох студентів. Кожен студент вчиться в певній групі, яка має свого старосту,
# та разом з іншими студентами групи вчить та здає певні предмети у певних викладачів,
# при цьому отримуючи деяку суму балів та державну оцінку. Студент може мати деякі захоплення (хоббі)

# Система повинна видавати звіти:
# Список студентів по групах,
# Список студентів які мають рейтинг від X до Y,

MAX_STUDENTS = 3
MAX_STUDENTS_IN_GROUP = 4
RATING = 1


# class Subject:
#     def __init__(self, subject_name, teacher_name, student, group=[], mark=0, state_assessment=0):
#         self.subject_name = subject_name
#         self.teacher_name = teacher_name
#         self.group = group
#         self.mark = mark
#         self.state_assessment = state_assessment
#         self.student = student
#
#     def set_mark(self, student, mark):
#         return ()

class Group:

    def __init__(self, group_name, headman, students_in_group=[]):
        self.group_name = group_name
        self.headman = headman
        self.students_in_group = students_in_group
        if len(self.students_in_group) > MAX_STUDENTS_IN_GROUP:
            print(f'Max number of students in a group is {MAX_STUDENTS_IN_GROUP}')

    def add_student_to_group(self, student):
        if len(self.students_in_group) < MAX_STUDENTS_IN_GROUP+1:
            self.students_in_group.append(student)
        else:
            print(f'The group {self.group_name} is full. Create new one, please.')

    def learn_subject(self, subject_name, teacher_name, time='in time'):
        self.subject_name = subject_name
        self.teacher_name = teacher_name
        self.time = time
        if self.time == 'in time':
            return f'Grope {self.group_name} successfully passed {self.subject_name} subject. {self.teacher_name} ' \
                   f'rated everyone 5 points'
        else:
            return f'Group {self.group_name} successfully passed \'{self.subject_name}\' subject. {self.teacher_name} '\
                   f'rated everyone 3 points'

    def __str__(self):
        string = f'The head man of the group \'{self.group_name}\' is{self.headman}and the group contains ' \
              f'follow students: '
        if len(self.students_in_group) == 0:
            return 'The group is empty'
        elif len(self.students_in_group) <= MAX_STUDENTS_IN_GROUP:
            for el in self.students_in_group:
                string += f'\n - {el}'
            return string


class DormitoryRoom:

    def __init__(self, room_number, students=[]):
        self.students = students
        self.room_number = room_number
        if len(self.students) > MAX_STUDENTS:
            print('Only 3 students can leave in one room.')

    def add_student_to_room(self, student):
        if len(self.students) < MAX_STUDENTS:
            self.students.append(student)
        else:
            print(f'The room {self.room_number} is full. Create new one, please.')

    def __str__(self):
        string = f'Room \'{self.room_number}\' contains follow students: '
        if len(self.students) == 0:
            return 'The room is empty'
        elif len(self.students) <= MAX_STUDENTS:
            for el in self.students:
                string += f'\n - {el}'
            return string
        else:
            return f'Max amount of students in a room is {MAX_STUDENTS}'


class Student:

    def __init__(self, surname, name, patronymic, student_card_number, day_of_birth, place_of_birth,
                 address, gender, marital_status, grants, rating=0, hobbies=[]):

        self.__surname = surname
        self.__name = name
        self.__patronymic = patronymic
        self.__student_card_number = student_card_number
        self.__day_of_birth = day_of_birth
        self.__place_of_birth = place_of_birth
        self.address = address
        self.__gender = gender
        self.marital_status = marital_status
        self.grants = grants
        self.hobbies = hobbies
        self.rating = rating

    def get_hobby(self):
        return self.hobbies

    def change_rating(self, mark):
        self.rating += mark
        return f'Student {self.__name} has rating {self.rating}'

    def show_rating(self):
        return self.rating

    def get_name(self):
        return self.__name

    def __str__(self):
        return f' {self.__name} {self.rating} '


p_1 = Student('Kli', 'Vla', 'Ole', '1', '07.10.1996', 'place of birth 1', 'Kiev 1', 'male', 'X', True)
p_2 = Student('Vaz', 'Liz', 'And', '2', '22.05.1997', 'place of birth 2', 'Kiev 2', 'female', 'XX', False)
p_3 = Student('Pod', 'Vad', 'Leo', '3', '05.04.1997', 'place of birth 3', 'Kiev 3', 'male', 'X', True)
p_4 = Student('Ste', 'Dia', 'Otc', '4', '28.02.1996', 'place of birth 4', 'Kiev 4', 'female', 'XX', True)
p_5 = Student('Dmi', 'Lit', 'Ale', '5', '31.05.1997', 'place of birth 5', 'Kiev 5', 'male', 'X', True)
p_6 = Student('Jul', 'Mel', 'Kir', '6', '25.12.1997', 'place of birth 6', 'Kiev 6', 'female', 'XX', True)
p_7 = Student('Vas', 'Pup', 'Edu', '7', '01.01.1991', 'place of birth 7', 'Kiev 7', 'male', 'X', True)


r_1 = DormitoryRoom('31 a', [p_1, p_2, p_3])
r_2 = DormitoryRoom('32 b', [p_4, p_5])
r_3 = DormitoryRoom('33 c')

r_2.add_student_to_room(p_6)

r_3.add_student_to_room(p_7)


g_1 = Group('IT 121', p_1, [p_1, p_2, p_3, p_4])

g_2 = Group('IT 122', p_5, [p_5, p_6])

g_2.add_student_to_group(p_7)

# print(g_1)
# print(g_2)
# print(g_1)
# print(r_1)
# print(r_2)
# print(r_3)

p_1.change_rating(3)
p_2.change_rating(5)
p_3.change_rating(1)
p_4.change_rating(2)
p_5.change_rating(7)
p_7.change_rating(9)
p_6.change_rating(10)

rate = [p_1, p_2, p_3, p_4, p_5, p_6, p_7]

for el in rate:

    print(f'{el.get_name()} - {el.show_rating()}')


# print(g_1.learn_subject('math', 'Nat A.L.', ''))
#
# print(p_1)
