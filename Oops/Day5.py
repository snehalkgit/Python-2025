# program 1 single inheritance
class Father:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sname = sn

    def displaySName(self):
        print(self.sname + self.lastName)
        
snehal = Son("snehal","kamble","snehal")
print(snehal.firstName)
print(snehal.lastName)
print(snehal.sname)
snehal.displayName()
snehal.displaySName()

# program 2
# multi-level

class GrandFather:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayName(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):

    def __init__(self, fn, ln,ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFName(self):
        print(self.fname + self.lastName)



class Son(Father):
    def __init__(self, fn, ln, ffn ,ssn):
        super().__init__(fn, ln, ffn)
        self.sname = ssn

    def displaySName(self):
        print(self.sname + self.lastName)


sonu = Son("manohar","deshpande","shirish","chinmay")

print(sonu.firstName)
print(sonu.lastName)
print(sonu.sname)
print(sonu.fname)

sonu.displayFName()
sonu.displaySName()
sonu.displayName()


# heriarchical inhertiance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln 

    def displayMname(self):
        print(self.firstName + self.lastName)

class Son(Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname  = ssn
    def displaySon(self):
        print(self.firstName + self.lastName)


class Daughter(Mother):
    def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname  = ddn
    def displayDaughter(self):
        print(self.firstName + self.lastName)


sonu  = Son("jyotsna","kamble","sonu")
monu = Daughter ("jyotsna","kamble","monu")

sonu.displayMname()
monu.displayDaughter()

sonu.displayMname()
monu.displayDaughter()



# multiple inheritance 



class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.fname = fn 
        self.lname = ln

    def displayFName(self):
        print(self.fname + self.lname)

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called .....")
        self.mname = fn 
        self.lname = ln

    def displayMName(self):
        print(self.mname + self.lname)

class Son(Mother,Father):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lname)


snehal1 = Son("kalayni","kamble","snehal2")






