numbers  = [11,22,33]
print(numbers)
print(type(numbers))

numbers = (11,22,3)
print(numbers)
print(type(numbers))

# stores the data by index
cities = ["pune","mumbai","bangalore"]
cities2 = "pune","mumbai","bangalore"
print(cities[0])
print(cities[1])

# mutable or immutable 
fruits = ["apple","mango","banana"]
fruitsB = ("apple","mango","banana")
# fruits[0] = "papaya"
# fruitsB[0] = "banana"
# tuple is fixed length

# element or not 
# country = ["india","pakistan","srilanka"]
# countryB = ("india","pakistan","srilanka")
# print("india" in country)
# print("India" in countryB)

# #len()
# print(len(country))
# print(len(countryB))

# # loops
# marks = [99,88,77,66]
# marksB = (11,22,33,44)

# # for range()
# for x in range(len(marks)):
#     #print(x)
#     print(marks[x])

# for x in range(len(marksB)):
#     #print(x)
#     print(marksB[x])

# # for loop

# for x in marksB:
#     print(x)

# for x in marks:
#     print(x)

# # while loop

# a1 = 0
# while(a1 < len(marks)):
#     #print(a1)
#     print(marks[a1])
#     a1 = a1 + 1 

# a1 = 0
# while(a1 < len(marksB)):
#     #print(a1)
#     print(marksB[a1])
#     a1 = a1 + 1 

k = (11,22,33,44)
x1,x2,x3,x4 = k
print(x1)
print(x2)
print(x3)
print(x4)


a = 11,
a1 = 11,12
a2 = (1,2)
print(type(a))
print(type(a1))
print(type(a2))

# slicing 
#          0        1         2          3        4
cities = ["pune","mumbai","bangalore","kolkata","chennai"]
#          -5       -4      -3           -2           -1
#cities[startIndex:EndIndex(not included):Steps]
# byDefault EndIndex - lastElement
# byDefault StartIndex - firstElement / firstIndex -0
# byDefault StepSize - 1 

print(cities[1:3])
print(cities[1:5])
print(cities[:4])
print(cities[1:])
print(cities[-4:-1])
print(cities[1:-1])
print(cities[0:5:2])
print(cities[::-1])
print(cities[4:1])
print(cities[-4:4])
print(cities[4:-4])