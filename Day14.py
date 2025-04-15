
# list comprehension 

# list comprehension ------ output list

# program  1
#[1,4,9,16,25]
for x in range(1,6):
    print(x)
e1 = [x * x for x in range(1,6)]
print(e1)

#[expression:loop:condition]
#program 2
lst = [2,4,55,66,77,88,99]
e2 = [x for x in lst if x % 2 == 0]
print(e2)

# program 3
lst = [2,4,55,66,77,88,99]
e3 = ["even" if x % 2 == 0 else "odd" for x in lst]
print(e3)


# program 4
names = ["snehal","sham","ram","satish","tanmay"]
e4 = [x.upper() for x in names]
print(e4)

# program 5
people = [
    {"name":"snehal","age":35},
    {"name":"sarika","age":27},
    {"name":"mayuri","age":26}
]
#[snehal,sarika,mayuri]
e4 = [x['name'] for x in people]
print(e4)

# only get me dict where age is between 25 - 30
e5 = [x for x in people if x['age'] >= 25 and x['age'] <= 30]
print(e5)

# name of person in list age above 35
e6 = [x['name'] for x in people if x['age'] >= 35]
print(e6)


# decorator , generators 