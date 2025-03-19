class Human:
    """Human class"""
    name: str = "Human_Yeshwanth_"
    def __init__(self, name):
        self.name = name

class Employee(Human):
    name:str = None
    def __init__(self, name):
        self.name = name
        print("Override by Evil Employee")
employee = Employee("yeshwanth")
print(employee.name)