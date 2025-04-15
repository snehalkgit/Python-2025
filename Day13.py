birthYear  = [2000,2001,2002,2000]
ages = []
for x in birthYear:
    age  = 2025 - x
    ages.append(age)
print(ages)

ages2 = [2025 - x for x in birthYear]
print(ages2)

age = lambda x :2025 -x 
ages2 = list(map(age,birthYear))
print(ages2)

# program 2
numbers = [1,2,3,4,5,6,7,8,9,10]
sqrt = lambda x: x * x
squares = list(map(sqrt,numbers))
print(squares)

# program 3

marks = [90,91,45,45,47,88,99,66,88]
above60 = []

for x in marks:
    if x > 60:
        above60.append(x)
print(above60)

above602 = [x for x in marks if x > 60]
print(above602)

above60 = lambda x : x > 60
above603 = list(filter(above60,marks))
print(above603)

transactions = [15,-5,66,77,-18,67,-45]
withdrawl = lambda x : x < 0
deposit = lambda x : x > 0
wr = list(filter(withdrawl,transactions))
print(wr)
dp = list(filter(deposit,transactions))
print(dp)

dp = [x for x in transactions if x > 0]
wr = [x for x in transactions if x < 0]
print(dp)
print(wr)

# program 4

numbers = [11,22,33]
total = 0
for x in numbers:
    total = total + x
print(total)

from functools  import reduce
total2 = reduce(lambda x,y:x+y,numbers,5)
print(total2)