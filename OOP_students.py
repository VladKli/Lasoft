# Кожен студент характеризується такими атрибутами : прізвище, імя, по  батькові, номер студентського квитка,
# рік народження, місце народження, адреса, стать, сімейний стан, стипендія, кімната в гуртожитку.
# В одній кімнати проживає до трьох студентів. Кожен студент вчиться в певній групі, яка має свого старосту,
# та разом з іншими студентами групи вчить та здає певні предмети у певних викладачів,
# при цьому отримуючи деяку суму балів та державну оцінку. Студент може мати деякі захоплення (хоббі)

# Система повинна видавати звіти:
# Список студентів по групах,
# Список студентів які мають рейтинг від X до Y,

MAX_STUDENTS = 3
MAX_STUDENTS_IN_GROUP = 5


class Subject:
    def __init__(self, subject_name, teacher_name):
        self.subject_name = subject_name
        self.teacher_name = teacher_name

    def __str__(self):
        return f'{self.subject_name}, {self.teacher_name}'


class Group:

    def __init__(self, group_name, headman, students_in_group=[]):
        self.group_name = group_name
        self.headman = headman
        self.students_in_group = students_in_group
        if len(self.students_in_group) < MAX_STUDENTS_IN_GROUP:
            self.students_in_group = students_in_group
        else:
            self.students_in_group = []
            raise Exception(f'Max number of students in a group is {MAX_STUDENTS_IN_GROUP}')

    def add_student_to_group(self, student):
        if len(self.students_in_group) < MAX_STUDENTS_IN_GROUP+1:
            self.students_in_group.append(student)
        else:
            raise Exception('Max number of students in a group is {MAX_STUDENTS_IN_GROUP}')

    def remove_student_from_group(self, student):
        if student in self.students_in_group:
            self.students_in_group.remove(student)
            print(f'Student {student.get_name()} was removed from the group {self.group_name}')
            return self.students_in_group
        else:
            raise Exception('There is no such student in the group.')

    def __str__(self):
        string = 'The group is empty'
        if len(self.students_in_group) > 0:
            string = f'The head man of the group {self.group_name} is{self.headman}' \
                     f'and the group contains follow students: '
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
                 address, gender, marital_status, grants, rating=0, hobbies=[], subjects={}):

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
        self.subjects = subjects
        self.rating = rating

    def learn_subject(self, subject, mark):
        self.subjects[subject.subject_name] = [subject, mark]
        return self.subjects[subject.subject_name]

    def get_avg_rating(self):
        a = []
        for subject in self.subjects:
            a.append(self.subjects[subject][1])
        return sum(a)

    def get_hobby(self):
        return self.hobbies

    def get_name(self):
        return self.__name

    def __str__(self):
        return f' {self.__name} {self.__surname} '


p_1 = Student('Kli', 'Vla', 'Ole', '1', '07.10.1996', 'place of birth 1', 'Kiev 1', 'male', 'X', True)
p_2 = Student('Vaz', 'Liz', 'And', '2', '22.05.1997', 'place of birth 2', 'Kiev 2', 'female', 'XX', False)
p_3 = Student('Pod', 'Vad', 'Leo', '3', '05.04.1997', 'place of birth 3', 'Kiev 3', 'male', 'X', True)
p_4 = Student('Ste', 'Dia', 'Otc', '4', '28.02.1996', 'place of birth 4', 'Kiev 4', 'female', 'XX', True)
p_5 = Student('Dmi', 'Lit', 'Ale', '5', '31.05.1997', 'place of birth 5', 'Kiev 5', 'male', 'X', True)
p_6 = Student('Jul', 'Mel', 'Kir', '6', '25.12.1997', 'place of birth 6', 'Kiev 6', 'female', 'XX', True)
p_7 = Student('Vas', 'Pup', 'Edu', '7', '01.01.1991', 'place of birth 7', 'Kiev 7', 'male', 'X', True)

s_math = Subject('Math', 'Alina T.')
s_read = Subject('Read', 'Alina T')
s_eng = Subject('English', 'Irina D')

p_1.learn_subject(s_math, 10)
p_1.learn_subject(s_read, 7)
p_1.learn_subject(s_eng, 8)
p_1.rating = p_1.get_avg_rating()

p_2.learn_subject(s_math, 1)
p_2.learn_subject(s_read, 7)
p_2.learn_subject(s_eng, 12)
p_2.rating = p_2.get_avg_rating()

p_3.learn_subject(s_math, 9)
p_3.learn_subject(s_read, 9)
p_3.learn_subject(s_eng, 0)
p_3.rating = p_3.get_avg_rating()

p_4.learn_subject(s_math, 11)
p_4.learn_subject(s_read, 10)
p_4.learn_subject(s_eng, 12)
p_4.rating = p_4.get_avg_rating()

p_5.learn_subject(s_math, 4)
p_5.learn_subject(s_read, 3)
p_5.learn_subject(s_eng, 4)
p_5.rating = p_5.get_avg_rating()

p_6.learn_subject(s_math, 9)
p_6.learn_subject(s_read, 7)
p_6.learn_subject(s_eng, 6)
p_6.rating = p_6.get_avg_rating()

p_7.learn_subject(s_math, 5)
p_7.learn_subject(s_read, 5)
p_7.learn_subject(s_eng, 3)
p_7.rating = p_7.get_avg_rating()

common_rating = dict()
common_rating[p_1.get_name()] = p_1.rating
common_rating[p_2.get_name()] = p_2.rating
common_rating[p_3.get_name()] = p_3.rating
common_rating[p_4.get_name()] = p_4.rating
common_rating[p_5.get_name()] = p_5.rating
common_rating[p_6.get_name()] = p_6.rating
common_rating[p_7.get_name()] = p_7.rating

print(sorted(common_rating.items(), key=lambda value: value[1], reverse=True))


# r_1 = DormitoryRoom('31 a', [p_1, p_2, p_3])
# r_2 = DormitoryRoom('32 b', [p_4, p_5])
# r_3 = DormitoryRoom('33 c')

# r_2.add_student_to_room(p_6)
#
# r_3.add_student_to_room(p_7)


g_1 = Group('IT 121', p_1, [p_1, p_2, p_3, p_4])

g_2 = Group('IT 122', p_5, [p_5, p_6])

g_2.add_student_to_group(p_7)

print(g_1)
print(g_2)

g_1.remove_student_from_group(p_2)
print(g_1)

# print(r_1)
# print(r_2)
# print(r_3)
