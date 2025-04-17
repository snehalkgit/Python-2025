class Calculator:

    # def addition(self,x,y):
    #     print(x+y)

    # def addition(self,x,y,z):
    # #     print(x+y+z)

    # def addition(self,x,y,z,a):
    #     print(x+y+z+a)

    def addition(self,a = None , b = None , c = None , d = None):
        if (a != None and b != None and c != None and d != None):
            print(a+b+c+d)
        elif(a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a+b)
        else:
            print("wrong input")



cal = Calculator()
cal.addition(133,4)
cal.addition(22,4,4)
cal.addition(23,43,42,15)


# overriding  method 
# same method , same signature but different class or has a relationship
class WorldBank:
    def loan(self):
        print("loan method called")
    def save(self):
        print("save method called")

class SBI(WorldBank):
    def loan(self):
        print("sbi loan method called")
    def save(self):
        print("sbi save method called")

hinganghat = SBI()
hinganghat.loan()
hinganghat.save()


