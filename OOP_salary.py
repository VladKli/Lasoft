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

    def __init__(self, position, personal_number, name, surname, father_name, pp_data, dob, place_of_birth, address,
                 salary=0, vacation=False):
        self.position = position
        self.personal_number = personal_number
        self.name = name
        self.surname = surname
        self.father_name = father_name
        self.pp_data = pp_data
        self.dob = dob
        self.place_of_birth = place_of_birth
        self.address = address
        self.salary = int(salary)
        self.vacation = vacation

    def get_name(self):
        return f'{self.name} {self.surname}'

    def credit_main_salary(self, working_hours, tariff_per_hour):
        self.salary += (int(working_hours) * int(tariff_per_hour))
        return self.salary

    def credit_bonus_part(self, tariff_per_hour, double_hours_amount=0, triple_hours_amount=0):
        self.salary += (double_hours_amount * Employee.DOUBLE * int(tariff_per_hour)) + \
                       (triple_hours_amount * Employee.TRIPLE * int(tariff_per_hour))
        return self.salary

    def get_salary(self):
        return self.salary

    def get_vacation(self):
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

emp_1 = Employee(developer.name, '855', 'Vla', 'Kli', 'Ole', '123EN321', '07.10.1996', 'smt. Rov', 'Kiev')
emp_2 = Employee(recruiter.name, '899', 'Liz', 'Vaz', 'And', '188EN921', '22.05.1997', 'Kiev', 'Kiev')
emp_3 = Employee(head_of_fin_dep.name, '1', 'Sve', 'Pri', 'Ale', '123EN321', '20.06.1975', 'smt. Rov', 'Kiev')
emp_4 = Employee(developer.name, '147', 'Vlad', 'Sho', 'Ser', '199EN321', '29.05.1996', 'Kiev', 'Kiev')

fin_dep = Department('Financial department', '123 456', emp_3.get_name(), [emp_1.get_name(), emp_2.get_name()])

fin_dep.remove_employee(emp_1.get_name())


emp_1.credit_main_salary(180, developer.get_tariff())

emp_1.credit_bonus_part(developer.get_tariff(), 1, 1)

emp_1.set_vacation()

emp_vacation = [emp_1.get_vacation(), emp_4.get_vacation()]


counter = 0

for emp in emp_vacation:
    if emp:
        counter += 1
    percent = (counter / len(emp_vacation)) * 100

print(percent)
