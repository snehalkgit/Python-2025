class person :
    Firstname = None
    Lastname  = None
    Age = None

    def talk(self):
        print('I am talking')
    def walk(self):
        print('i am walking')

snehal = person()
print(snehal.Firstname)
snehal.walk()
snehal.talk()

# Program 2
# Setting the class attribute at the time object creation

class Person2:
    # constructor
    def __init__(self,fn,ln,age):
        self.firstName = fn 
        self.lastName = ln 
        self.age = age 

    def displayName(self):
        print(self.firstName + self.lastName)
    
amol2 = Person2("harsha","kale", "23")
amol2.displayName()
print(amol2.firstName)
print(amol2.lastName)
print(amol2.age)

chinmay2 = Person2('snehal','kamble',34)

class Person4:
    country = "India"
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

snehal  = Person4("snehal","kamble")
nilesh  = Person4("nilesh","Dangt")
print(snehal.firstName)
print(snehal.lastName)
print(snehal.country)
snehal.country ="Bharat"

print(snehal.country)
print(nilesh.country)

