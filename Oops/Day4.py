 # program 1 single inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstanme = fn 
        self.lastname = ln 

    def displayname(self):
       print(self.firstanme + self.lastname)      
class Son(Father):
    def __init__(self, fn, ln,sn):
        super().__init__(fn, ln)
        self.sname = sn 
    def displaySName(self):
        print(self.sname + self.lastname)    

snehal = Son ("kawadu","kamble","snehal") 
print(snehal.firstanme)
print(snehal.lastname)
print(snehal.sname)


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


snehal = Son("kakak","male","kawadu","snehal")

print(snehal.firstName)
print(snehal.lastName)
print(snehal.sname)
print(snehal.fname)

snehal.displayFName()
snehal.displaySName()
snehal.displayName()


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


sonu  = Son("jyptsna","kamble","snehal")
monu = Daughter("jyotsna","kamble","monu")

sonu.displayMname()
sonu.displaySon()

monu.displayMname()
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


snehal =Son ("jyotsna","kamble","chkawad")
