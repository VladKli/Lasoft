# Кожен студент характеризується такими атрибутами : прізвище, імя, по  батькові, номер студентського квитка,
# рік народження, місце народження, адреса, стать, сімейний стан, стипендія, кімната в гуртожитку.
# В одній кімнати проживає до трьох студентів. Кожен студент вчиться в певній групі, яка має свого старосту,
# та разом з іншими студентами групи вчить та здає певні предмети у певних викладачів,
# при цьому отримуючи деяку суму балів та державну оцінку. Студент може мати деякі захоплення (хоббі)

class Grope:



# Система повинна видавати звіти:
# Cписок студентів по групах,
# Cписок студентів які мають рейтинг від X до Y,

class Student:

    def __init__(self, __surname, __name, __patronymic, __student_card_number, __day_of_birth, __place_of_birth,
                 address, __gender, marital_status, grants, dormitory_room):

        self.surname = __surname
        self.name = __name
        self.patronymic = __patronymic
        self.student_card_number = __student_card_number
        self.day_of_birth = __day_of_birth
        self.place_of_birth = __place_of_birth
        self.address = address
        self.gender = __gender
        self.marital_status = marital_status
        self.grants = grants
        self.dormitory_room = dormitory_room


class DormitoryRoom:

    @staticmethod
    def set_student(__student_card_number):
        rooms = []
        if len(rooms) < 3:
            rooms.append(__student_card_number)
        else: