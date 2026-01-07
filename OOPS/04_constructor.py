class Employee: 
    language = "Py" # This is a class attribute
    salary = 1200000
    
    def __init__(self,name,salary,language):#dunder method which is automatically called, dunder method is a method called for double underscore functions.
        self.name= name
        self.salary = salary 
        self.language = language
        print("I am creating this object")
         
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet(self):
        print("Good morning")
        
        
harry = Employee("Harry", 1300000, "Javascript")
#harry.name= "Harry"
print(harry.language, harry.salary, harry.name)

#rohan = Employee()