# variable 
# int , float , boolean str
# type --- comparison , logical operator
# conditional statement , loops for while 
# list - CRUD  -- create , retrive , update ,delete / loop - methods
# dict - CRUD   --  loop - methods
# tuple - Cr - methods  CRUD
# str - CRUD , Methods

fn =  "snehal"
e = fn.upper()
print(e)

ln = "kawadu"
e2 = ln.lower()
print(e2)

mn = "Harsha"
e3 = mn.capitalize()
print(e3)

title = "I am learning sql"
e4 = title.title()
print(e4)


# String format methds 
f = " goa "
print(len(f))
e5 = f.strip()
print(e5)
print(len(e5))

f2 = " goa "
print(len(f2))
e6 = f2.lstrip()
print(e6)

f3 = "goa "
print(len(f3))
e7 = f3.rstrip()
print(len(e7))

s = "hello"
e8 = s.center(10,'-')
print(e8)

#  --hello---

s = "helloooooo"
e9 = s.ljust(10,'-')
print(e9)

s = "hello"
e10 = s.rjust(10,'-')
print(e10) 

#zfill
ide = '9999'
e = ide.zfill(5)
print(e)

# String check methods 

print('abc'.isalpha())
print('123'.isnumeric())
print('123'.isalnum())
print('123aaa'.isalnum())
print('aaa'.isalnum())
print(''.isalnum())
print('abc'.islower())
print('ABC'.isupper())
print(" ".isspace())
print("I Am Learning python".istitle())

# seach methods 
#0123456
#"hello world"
s = "hello world"
e = s.find("world")
print(e)

s = "hello world hello"
j = s.rfind("hello")
print(j)

city = "pune"

# 0  1  2  3
# p  u  n  e
print("hello")
d = city.index("p")
print(d)
print("bye")


s = "hello world cool"
y = s.rindex("hello")
print(y)


j = "hello hello hello"
h = j.count("l")
print(h)


info = "i am learning sql"
e = info.replace("js","python")
print(e)

# splitting and join methods

s = "apple,banana,grape"
e = s.split(',')
print(e)


info = ["snehal","kawadu","2441"]
r = "-".join(info) # chinmay@deshpande@7709192441
print(r)


h = "snehal"
e = h.startswith('sn')
print(e)

f = h.startswith('K')  
print(f)

b = "kaka"
f2 = b.endswith('kaka')
f3 = b.endswith('k')
print(f2)
print(f3)
 