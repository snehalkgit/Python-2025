# program 1
birthYear = [2000,2001,2002,2003]
ages = [] # [25,24,23,22]
for x in birthYear:
    age = 2025 - x
    ages.append(age)
print(ages)

# list comprehension
# output will always be a list
#[epression:loop:condition]
e = [2025 - x for x in birthYear]
print(e)


# program 2
numbers = [11,22,33,44,55]
e2 = [x + 1 for x in numbers]
print(e2)

# program 3
marks = [45,43,33,40,38,39,54]
above40 = []
for x in marks:
    if x > 40:
        above40.append(x)
print(above40)

#[epression:loop:condition]
e3 = [x for x in marks if x > 40]
print(e3)

# program 3
transactions = [90,-89,44,55,66,34,-13,-45]
deposit = [x for x in transactions if x > 0]
print(deposit)
withdrawl = [x for x in transactions if x < 0]
print(withdrawl)


#even
#program 4
listA  = [33,33,44,55,66,77]
e = [x for x in listA if x % 2 == 0]
print(e)

#program 5
listA  = [33,33,44,55,66,77]
#[odd,odd,even,odd,even,odd]
e = ["even" if x % 2 == 0 else "odd" for x in listA]
print(e)

#program 6
ages = [44,55,33,44,12,33,11,22,14]
e4 = ["candrive"  if x >= 18 else "cannot drive" for x in ages]
print(e4)