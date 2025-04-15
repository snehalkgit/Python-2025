## method

# ## instance method
# accessor method 
#  class meathod
# static method 


class person :
   # class level attribute 
        country = " india"
        count = 0 

        def __init__(self,fn,ln,age):
                self.firstname = fn 
                self.lastname = ln 
                self.age = age 
                person.count = person.count + 1
                #instant method 
        def displayname(self):
             print(self.firstname + self.lastname)
             return self.firstname + self.lastname
        
            #instant - update age - mutator method 
        def updateage(self,ag):
               self.age= ag
               #class level method 
        @classmethod
        def updatecountry(cls, countryname):
               cls.country = countryname

        @staticmethod
        def totalnumberofcounts():
              print(person.count)
            

snehal = person("snehal","kamble",24)
person.totalnumberofcounts()



class Bank:
    country = " china"
    count = 0 
    def __init__(self,fullname, balance):
          self.balance = balance 
          self.fullname = fullname 
          self.transition = []
          Bank.count = Bank.count+1

    #method to retrive the balance 
    def getbalance(self):
          return self.balance

    #method to deposit

    def deposit(self,amt):
          self.balance = self. balance + amt   
          self.transition.append(amt)
          return self.balance  

#methpod to withdraw()

def withdraw(self,amt):
    if amt < self.blance:
     self.transaction.append(-amt)
    else:
          print("insufficient balance")
          return self.balance 
    
     
  
    #method to show last 5 transaction 
    def last_five_transactions(self):
        return self.transactions[-5::]

    #method to show number of accounts created
    @staticmethod
    def totalAccounts():
        return Bank.count

    # method to change country name for all acc holders
    @classmethod
    def changeCountry(cls,countryName):
        cls.country = countryName

amol = Bank("amol",12300)  
chinmay = Bank("chinmay",10000000000000)  
gauri = Bank("gauri",12300000000)  
sarika = Bank("sarika",12300000000)  
vedant = Bank("vedant",123000000000000000)  


amol.deposit(11)  
amol.deposit(10)  
amol.deposit(10)
amol.deposit(1000)
amol.deposit(100000)  

print(amol.last_five_transactions())
print(amol.country)
Bank.changeCountry("bharat")
print(amol.country)
accounts = Bank.totalAccounts()
print(accounts)

