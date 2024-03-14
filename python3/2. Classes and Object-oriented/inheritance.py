class Employee:
    __slots__ = ('name', 'age', 'salary')

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary +=  self.salary * (percent / 100)


class SlotsInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, '__slots__')


class Tester(Employee):
    def run_tests(self):
        print(f'Testing is started by {self.name}')
        print('Test done.')


class Developer(SlotsInspectorMixin, Employee):
    __slots__ = ('framework',)

    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus


test = Tester('Toan', 25, 1000)
test.run_tests()

developer = Developer('Toan Phay', 28, 2000, 'django')
developer.increase_salary(20, 20)
print(developer.salary)
print(developer.has_slots())
print(developer.__dict__)