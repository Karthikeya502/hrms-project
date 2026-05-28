class Employee:
    def __init__(self, name, age, salary, designation):
        self.name = name
        self.age = age
        self.salary = salary
        self.designation = designation
    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Salary: {self.salary}')
        print(f'Designation: {self.designation}')


employee_id_1= Employee('Mohit', 20,50000,'HR')
employee_id_1.display()
