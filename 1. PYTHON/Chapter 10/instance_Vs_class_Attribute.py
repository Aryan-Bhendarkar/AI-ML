class Employee:
    language =  "Py"
    salary =  120000
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    #  def greet(self):
    #     print("Good Morning...")

    #  It doesn't need object or aything 
    @staticmethod
    def greet():
        print("Good Morning...")

harry = Employee()
harry.language = "JavaScript"
print(harry.language)
harry.getInfo()
Employee.getInfo(harry)

harry.greet()
# harry.greet() Gives error if we don't add self as parameter so always add self 