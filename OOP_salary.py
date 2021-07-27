class Department:
    def __init__(self, department_name, cod, manager_name, employee=[]):
        self.department_name = department_name
        self.cod = cod
        self.manager_name = manager_name
        self.employee = employee

    def get_employees(self):
        list_of_employee = f'{self.department_name} is empty'
        if len(self.employee) > 0:
            list_of_employee = f'{self.department_name} contains follow employee: '
            for emp in self.employee:
                list_of_employee += f'\n - {emp}'
        return list_of_employee

    def add_employee_to_dep(self, employee_name):
        return self.employee.append(employee_name)

    def remove_employee(self, employee_name):
        return self.employee.remove(employee_name)

    def __str__(self):
        return f'Department: {self.department_name} \nmanager: {self.manager_name}\ncod: {self.cod}'


class Employee:
    def __init__(self, position, personal_number, name, surname, father_name, pp_data, dob, place_of_birth, address):
        self.position = position
        self.personal_number = personal_number
        self._name = name
        self._surname = surname
        self._father_name = father_name
        self._pp_data = pp_data
        self._dob = dob
        self.place_of_birth = place_of_birth
        self.address = address

    def get_name(self):
        return f'{self._name} {self._surname}'

    def __str__(self):
        return f'{self.position}, {self.personal_number}, {self._name} {self._surname} {self._father_name}, ' \
               f'{self._pp_data}, {self._dob}, {self.place_of_birth}, {self.address}'


class Position:
    def __init__(self, name, tariff_per_hour):
        self.name = name
        self.tariff_per_hour = tariff_per_hour

    def get_info(self):
        return f'{self.name} has tariff {self.tariff_per_hour} euro per hour.'

    def change_tariff(self, new_tariff):
        self.tariff_per_hour = new_tariff
        return self.tariff_per_hour


developer = Position('Developer', '10')
recruiter = Position('Recruiter', '8')
head_of_fin_dep = Position('Head of financial department', '15')

emp_1 = Employee(developer.name, '855', 'Vla', 'Kli', 'Ole', '123EN321', '07.10.1996', 'smt. Rov', 'Kiev')
emp_2 = Employee('recruiter', '899', 'Liz', 'Vaz', 'And', '188EN921', '22.05.1997', 'Kiev', 'Kiev')
emp_3 = Employee('head of financial department', '1', 'Sve', 'Pri', 'Ale', '123EN321', '20.06.1975', 'smt. Rov', 'Kiev')

fin_dep = Department('Financial department', '123 456', emp_3.get_name(), [emp_1.get_name(), emp_2.get_name()])

print(fin_dep.get_employees())
print(fin_dep)

fin_dep.remove_employee(emp_1.get_name())
print(fin_dep.get_employees())

print(emp_1)

developer.change_tariff('20')
print(developer.get_info())