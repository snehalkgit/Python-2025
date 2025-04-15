
# setA =  {11,22,33}
# setB = {33,44,55}
# setC  = setA.union(setB)
# print(setC)

# setD = {11,22,33}
# setE = {11,55,33,77}


# # setR = setD.intersection(setE)
# # # print(setR)

# # setD.intersection_update(setE)
# # print(setD)

# # setE.intersection_update(setD)
# # print(setE)

# # program 2

# setG = {22,33,44}
# setH = {33,88,99}

# # setZ  = setG.difference(setH)
# # print(setZ)

# # setK = setH.difference(setG)
# # print(setK)

# # setH.difference_update(setG)
# # print(setH)

# setG.difference_update(setH)
# print(setG)


# # program 3

# setQ = {44,55,66}
# setL = {99,77,88,44}

# # setY = setQ.symmetric_difference(setL)
# # print(setY)

# setQ.symmetric_difference_update(setL)
# print(setQ)


# setA = {11,22,33}
# setB = {22,33}
# print(setB.issuperset(setA))
# print(setA.issuperset(setB))
# print(setA.issubset(setB))
# print(setB.issubset(setA))

# setA = {111,33,44}
# setB = {11,22,77}
# e = setA.isdisjoint(setB)
# print(e)

# setA  = {44,55,66,77}
# setB = {77,88,99,44}

# t = setA.pop()
# print(t)
# print(setA)


# print("hello")
d = {23,44,55,66,77}
# d.discard(444)
# print(d)
# print("bye")


# print("hello")
# d.remove(557)
# print(d)
# print("bye")

d = {23,44,55,66,77}
d.add(666)

b = {11,22,33,44,55,66,77}
b.update([2222,3333])
b.update([233123123,66666,4444,555])
b.update({91,92,92})
print(b)


# list ,string ,tuple , set , dictionary 

# list comprehension

birthYear = [2000,2001,2002,2003]
ages = []
#[25,24,23,22]
for x in birthYear:
    age = 2025 - x
    ages.append(age)
print(ages)

marks  = [77,90,92,93,94,66]
#[90,92,93,94]
above90 = []
for x in marks:
    if x > 90:
        above90.append(x)
print(above90)


numbers = [11,22,33]
total = 0

for x in numbers:
    total = total + x 
print(total)











