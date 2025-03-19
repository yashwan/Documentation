

class Employ:
    company_name:str = "Riktam"
    @classmethod
    def change_company_name(cls, name:str):
        cls.company_name = name


employee:Employ = Employ()
print(employee.company_name) 
employee.change_company_name("EY")
print(employee.company_name)