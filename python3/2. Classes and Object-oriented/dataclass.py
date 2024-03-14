from dataclasses import dataclass


# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client

@dataclass(slots=True)
class Project:
    name: str
    payment: int
    client: str

    def get_name(self):
        print(self.name)

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("DJango app", 2000, "ToanTrugen")
e = Employee("Toan", 25, 100, p)

print(e.project)
p.get_name()