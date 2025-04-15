# int as and int as return 
def add(a):
    return a + a
e = add(1)
print(e)

# float as param and float as return type 
def addB(b):
    return b + b
e2 = addB(12.3)
print(e2)

# string as a parameter and string as return type 
def greet(word):
    return "hello" + word
e3 = greet("good morning !")
print(e3)

# list a parameter and list as return type 
cities = ["wardha","pune","mumbai"]
def addElementToList(lst):
    lst.append("nagpur")
    return lst
e4 = addElementToList(cities)
print(e4)

# boolean as parameter and boolean as return 
def canDrive(age,haveVehicle):
    if age >= 18 and haveVehicle:
        return True
    else:
        return False
e5 = canDrive(18,True)
print(e5)

# dict as parameter and dict as return type

info = {"firstNname":"chinmay","lastName":"deshpande"}
def addCity(dic):
    dic.update({"city":"pune"})
    return dic
e6 = addCity(info)
print(e6)

# tuple as parameter and tuple as return tupe

tupleA = (11,22,33)

def addValueTuple(tupA):
    # (11,22,33)
    tupA = list(tupA)  #[11,22,33]
    print(tupA)
    tupA.append(44) #[11,22,33,44]
    f = tuple(tupA) # (11,22,33,44)
    return f
e7 = addValueTuple(tupleA)
print(e7)

# set as parameter and set as return type 
setA  = {11,22,33}
def addElementToSet(setB):
    setB.add(44)
    return setB

e7 = addElementToSet(setA)
print(e7)

# default parameter 
def add(x=1,y=1):
    print(x+y)
add(12,3)
add()

# postional parameter 
def sub(x,y):
    print(x-y)
sub(500,50) # -450
sub(y=400,x= 300)

# args 
def addall(*args):
    print(args)
    print(sum(args))
    total = 0
    for x in args:
        total = total + x
    print(total)
addall(1,2,3,3,4,5,6,7,8,3,5,6,7,8,4,5)

# **kwargs
def showInfo(**kwargs):
    print(kwargs)
showInfo(name="chinmay",lastName="deshpande",age=23)

# lambda function

def add(a,b):
    print(a+b)
add(12,2)

add = lambda x,y:x+y
add(12,3)

x = 10
print(x)
q  = lambda x:x*x
print(q)
q(2)

# function as parameter 
add = lambda x,y:x+y
def addition(fn,x,y):
   #fn = lambda x,y:x+y
   # x = 10
   # y = 7
   sum =  fn(x,y)
   return sum

s = addition(add,10,7)
print(s)


# function as return type
def subtraction():
    return lambda x:x-x
sub = subtraction()
print(sub)
e = sub(1)
print(e)




# map()

# filter()

# reduce()