from datetime import date

class Employee:
    minimum_wage = 1000

    @classmethod
    def change_minimum_wage(cls, new_wage):
        if new_wage > 3000:
            raise ValueError("Company is bankrupt")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name , dob):
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, "developer 2",cls.minimum_wage)

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    def increase_salary(self, percent):
        self.salary +=  self.salary * (percent / 100)

    def __str__(self):
        return f'{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}'

    def __repr__(self):
        return f'Employee ({repr(self.name)}, {repr(self.age)}, {repr(self.position)}, {repr(self.salary)})'

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f"Minimum wage is ${Employee.minimum_wage}")
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

# e = Employee()
# print(e)
# print(e.name)
# print(e.__dict__)
# print(e.__class__)

employee1 = Employee('Toan', 25, 'developer', 1000)
employee2 = Employee('Toan Phay', 35, 'developer', 2000)
# employee2.increase_salary(20)
print(Employee.minimum_wage)
Employee.change_minimum_wage(200)
print(Employee.minimum_wage)
employee2.salary = 200

print(employee2)
print(repr(employee2))
print(eval(repr(employee2)))

print("-------------")

e = Employee.new_employee('Toan 2', date(1995, 8, 13))
print(e.name)
print(e.age)
print(e.minimum_wage)