
# single inheritance

class Student:
    def __init__(self,fn,ln):
        self.firsName  = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firsName + self.lastName)

class Teacher(Student):
    salary = 1000
    def displaySalary(self):
        print(self.salary)


snehal = Teacher("amit","bhure")
print(snehal.salary)
print(snehal.firsName)
print(snehal.firsName)
snehal.displayName()
snehal.displaySalary()



# incorrect way 
# class Teacher:
#     def __init__(self,fn,ln,salary):
#         self.firsName  = fn 
#         self.lastName = ln 
#         self.salary = salary

#     def displayName(self):
#         print(self.firsName + self.lastName)

#     def displaySalary(self):
#         print(self.salary)

    
# Program 2
# parent contructor and child also having constructor

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self, fn, ln,salary):
        super().__init__(fn,ln)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

shreya = Teacher("shreya ","tamgadge",1000)
print(shreya.firstName)
print(shreya.lastName)
print(shreya.salary)

shreya.displaySalary()
shreya.displayName()    
