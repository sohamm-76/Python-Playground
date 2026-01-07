class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet(self):
        print("Good morning")
        
        
harry = Employee()
harry.language = "Javascript" # This is an instance attribute
print(harry.language, harry.salary)
harry.getInfo()
harry.greet()
#Employee.getInfo(harry)