class Employee:
    language = "Python"
    salary = 120000

    def __init__(self, name, salary, language): # dunder Operator => automatically called 
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.langauge}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning !!!")
    

harry = Employee("harry" , 95482442,'JS')
print(harry.language,harry.name,harry.salary)
