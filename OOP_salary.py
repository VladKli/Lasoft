from datetime import date, timedelta


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

    def __init__(self, position, personal_number, name, surname, father_name, pp_data, dob, place_of_birth, address,
                 hire_date, salary=0, vacation=False):
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
        self.vacations = {'date_start': date(1111, 1, 1), 'date_end': date(1111, 1, 1)}

    def add_work_hour_per_day(self, hours):
        return self.work_hours_per_week.__add__(hours)

    def get_name(self):
        return f'{self.name} {self.surname}'

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

    def get_vacation(self, date_start, date_end):
        return self.vacation

    def set_vacation(self):
        self.vacation = True
        return self.vacation

    def finish_vacation(self):
        self.vacation = False
        return self.vacation

    # def get_percent_of_vacation_in_dep(self, department_name, employee):
    #     counter = 0
    #     percent = 0
    #     for emp in employee:
    #         if self.vacation:
    #             counter += 1
    #             percent = counter % len(employee) * 100
    #             return percent
    #         else:
    #             return counter

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

emp_1 = Employee(developer.name, '855', 'Vla', 'Kli', 'Ole', '123EN321', '07.10.1996', 'smt. Rov', 'Kiev', date(2020, 8, 4))
emp_2 = Employee(recruiter.name, '899', 'Liz', 'Vaz', 'And', '188EN921', '22.05.1997', 'Kiev', 'Kiev', date(2020, 1, 1))
emp_3 = Employee(head_of_fin_dep.name, '1', 'Sve', 'Pri', 'Ale', '123EN321', '20.06.1975', 'smt. Rov', 'Kiev', date(2020, 1, 1))
emp_4 = Employee(developer.name, '147', 'Vlad', 'Sho', 'Ser', '199EN321', '29.05.1996', 'Kiev', 'Kiev', date(2020, 1, 1))


# print(date.today() - timedelta(days=365))

list_of_employee = [emp_1, emp_2, emp_3, emp_4]


def set_vacation(employee, vacation_period=[], list_of_employees=[]):
    if employee.hire_date <= (date.today() - timedelta(days=365)):
        exist_employees = set(list_of_employees).difference(employee)
        percent = 0
        for emp in exist_employees:
            if vacation_period[0] <= (emp.vacations['date_start'] or emp.vacations['date_end']) <= vacation_period[1]:
                percent += 1
    employee.vacations['date_start'] = vacation_period[0]
    employee.vacations['date_end'] = vacation_period[1]
    return employee.vacations


print(set_vacation(emp_1, [date(2021, 1, 1), date(2021, 12, 1)], list_of_employee))


# fin_dep = Department('Financial department', '123 456', emp_3.get_name(), [emp_1.get_name(), emp_2.get_name()])
#
# fin_dep.remove_employee(emp_1.get_name())
#
#
# emp_1.credit_main_salary(180, developer.get_tariff())
#
# emp_1.credit_bonus_part(developer.get_tariff(), 1, 1)
#
# emp_1.set_vacation()
#
# emp_vacation = [emp_1.get_vacation(), emp_4.get_vacation()]


# counter = 0
#
# for emp in emp_vacation:
#     if emp:
#         counter += 1
#     percent = (counter / len(emp_vacation)) * 100
#
# print(percent)
