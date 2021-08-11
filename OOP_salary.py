from datetime import date, timedelta
from random import random


class Department:
    def __init__(self, department_name, cod, manager_name, employees=[]):
        self.department_name = department_name
        self.cod = cod
        self.manager_name = manager_name
        self.employees = employees

    def get_employees(self):
        list_of_employee = f'{self.department_name} is empty'
        if len(self.employees) > 0:
            list_of_employee = f'{self.department_name} contains follow employee: '
            for emp in self.employees:
                list_of_employee += f'\n - {emp}'
        return list_of_employee

    def add_employee_to_dep(self, employee_name):
        return self.employees.append(employee_name)

    def remove_employee(self, employee_name):
        return self.employees.remove(employee_name)

    def __str__(self):
        return f'Department: {self.department_name} \nmanager: {self.manager_name}\ncod: {self.cod}'


class Employee:

    DOUBLE = 2
    TRIPLE = 3
    DEFAULT_WORK_HOURS_PER_WEEK = 40
    VACATION_DAYS = 28

    def __init__(self, position, personal_number, name, surname, father_name, pp_data, dob, place_of_birth, address,
                 hire_date, salary=0, vacation=False):
        self.id = random()
        self.position = position
        self.personal_number = personal_number
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.pp_data = pp_data
        self.dob = dob
        self.place_of_birth = place_of_birth
        self.address = address
        self.hire_date = hire_date
        self.base_salary = int(salary)
        self.vacation = False
        self.work_hours_per_week = Employee.DEFAULT_WORK_HOURS_PER_WEEK
        self.vacations = [{'date_start': date(1, 1, 1), 'date_end': date(1, 1, 1)}]
        self.vacation_helper = False

# {'date_start': date(1111, 1, 1), 'date_end': date(1111, 1, 1)}, {'date_start': date(1111, 1, 1), 'date_end': date(1111, 1, 1)}

    def add_work_hour_per_day(self, hours):
        return self.work_hours_per_week.__add__(hours)

    def get_name(self):
        return f'{self.name} {self.surname}'

    def get_vacation_dates(self):
        list_of_dates = []
        for dates in self.vacations:
            for el in dates:
                list_of_dates.append(dates['date_start'])
        return list_of_dates

    def get_vacation_days(self):
        days = 0
        for _v in self.vacations:
            days += (_v['date_end'] - _v['date_start']).days
        return days

    def set_vacation(self, date_start, date_end):
        new_days = (date_end - date_start).days
        if self.hire_date <= (date.today() - timedelta(days=365)) and self.get_vacation_days() + new_days <= self.VACATION_DAYS:
            self.vacations.append({'date_start': date_start, 'date_end': date_end})
            self.vacation = True
        else:
            self.vacation = False
            raise Exception('It is not possible to set the vacation.')

    def credit_main_salary(self, working_hours, tariff_per_hour):
        self.base_salary += (int(working_hours) * int(tariff_per_hour))
        return self.base_salary

    def credit_bonus_part(self, tariff_per_hour, double_hours_amount=0, triple_hours_amount=0):
        self.base_salary += (double_hours_amount * Employee.DOUBLE * int(tariff_per_hour)) + \
                       (triple_hours_amount * Employee.TRIPLE * int(tariff_per_hour))
        return self.base_salary

    def get_salary(self):
        return self.base_salary

    def add_work_hours_per_week(self, hours):
        self.work_hours_per_week.__add__(hours)

    def get_vacation(self):
        if self.hire_date <= (date.today() - timedelta(days=365)):
            return True
        else:
            raise Exception('Current employee has not worked at company 1 year yet.')

    def __str__(self):
        return f'{self.position}, {self.personal_number}, {self.name} {self.surname} {self.father_name}, ' \
               f'{self.pp_data}, {self.dob}, {self.place_of_birth}, {self.address}, {self.salary}, {self.vacation}'


class Position:
    def __init__(self, name, tariff_per_hour):
        self.name = name
        self.tariff_per_hour = tariff_per_hour

    def get_tariff(self):
        return self.tariff_per_hour

    def change_tariff(self, new_tariff):
        self.tariff_per_hour = new_tariff
        return self.tariff_per_hour


developer = Position('Developer', '10')
recruiter = Position('Recruiter', '8')
head_of_fin_dep = Position('Head of financial department', '15')

emp_1 = Employee(developer.name, '855', 'Vlad', 'Kli', 'Ole', '123EN321', '07.10.1996', 'smt. Rov', 'Kiev', date(2019, 8, 4))
emp_2 = Employee(recruiter.name, '899', 'Liza', 'Vaz', 'And', '188EN921', '22.05.1997', 'Kiev', 'Kiev', date(2020, 1, 1))
emp_3 = Employee(head_of_fin_dep.name, '1', 'Sveta', 'Pri', 'Ale', '123EN321', '20.06.1975', 'smt. Rov', 'Kiev', date(2020, 1, 1))
emp_4 = Employee(developer.name, '147', 'Vlad', 'Sho', 'Ser', '199EN321', '29.05.1996', 'Kiev', 'Kiev', date(2021, 1, 1))


list_of_employee = [emp_1, emp_2, emp_3, emp_4]

# emp_1.set_vacation(date(2021, 1, 1), date(2021, 1, 25))
# emp_2.vacations = ({'date_start': date(2021, 1, 2), 'date_end': date(2021, 1, 5)})
# emp_3.vacations = ({'date_start': date(1, 1, 1), 'date_end': date(1, 12, 1)})
# emp_4.vacations = ({'date_start': date(1, 1, 1), 'date_end': date(1, 12, 1)})

# print(emp_2.vacations[0])
# print(emp_1.get_vacation_days())


def set_vacation(employee, date_start, date_end, list_of_employees=[]):
    count = []
    for emp in list_of_employees:
        for el in emp.get_vacation_dates():
            if date_start <= el <= date_end:
                emp.vacation_helper = True
        count.append(emp.vacation_helper)
    percentage = ((sum(count) + 1) / len(list_of_employees) * 100)
    if percentage <= 30:
        employee.set_vacation(date_start, date_end)
    else:
        raise Exception(f'It is not possible to take a vacation for {employee.name}.')


set_vacation(emp_1,  date(2021, 1, 1), date(2021, 1, 25), list_of_employee)
print(emp_1.vacations)

set_vacation(emp_2,  date(2021, 2, 1), date(2021, 2, 20), list_of_employee)
print(emp_2.vacations)

set_vacation(emp_3,  date(2021, 5, 5), date(2021, 5, 22), list_of_employee)
print(emp_3.vacations)

set_vacation(emp_4,  date(2021, 5, 5), date(2021, 5, 22), list_of_employee)






# print(set_vacation(emp_1, list_of_employee))
# print(list_of_employee)



