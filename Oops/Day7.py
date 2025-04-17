# ducking typing 
# operator overloading
# method overloading
# method overriding 

#program 

class Duck :
    def talk(self):
        print("quack quack")
 
class Human :
    def talk(self):
        print("hi hello") 

def call_talk(obj):
    obj.talk()

a = Duck()
b = Human()

call_talk(a)
call_talk(b)

# program 2
class Duck:
    def talk(self):
        print("Quack Quack")
class Human:
    def talk(self):
        print("Hi hello")
class Dog:
    def bark(self):
        print("Bow Bow")

def call_talk(obj):
    #obj.talk()
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
d = Duck()
h = Human()
c = Dog()

call_talk(c)
call_talk(d)
call_talk(h)


class Bookx:
    def __init__(self,pages):
        self.pages = pages 

    def __add__(self,others):
        return self.pages + others.pages
    
    def __sub__(self,others):
        return self.pages - others.pages
    
class Booky:
    def __init__(self,pages):
        self.pages = pages 

    def __gt__(self,others):
        return self.pages > others.pages
    
    
x = Bookx(200)
y = Booky(100)
        
print(x.pages+y.pages)
print(x+y)
print(x-y)
print(y > x)


# program 4
# overloading 


# class Cal:
#     def addition(self,x,y):
#         print(x+y)
    
#     def addition(self,x,y,z):
#         print(x+y+z)
    
#     def addition(self,x=None,y=None,z=None,a=None):
#         if(x != None and y != None and z != None and a != None):
#             print(x+y+z+a)
#         elif(x != None and y != None and z != None):
#             print(x+y+z)
#         elif(x != None and y != None):
#             print(x+y)

# a = Cal(12,4)
# b = Cal(12,4,3)
# c = Cal(12,4,3,4)




# overriding 
class Bank:
    def save(self):
        print("Bank save called")
    def loan(self):
        print("Banl loan called")

class SBI(Bank):
    def save(self):
        print("SBI Bank save called")
    def loan(self):
        print("SBI Bank loan called")

a = SBI()

a.loan()
a.save()

