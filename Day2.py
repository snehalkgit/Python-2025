#          0        1       2       3
names = ["sarika","ninad","mohan","ninad"]
print(names)
print(type(names))

# program 2
# names[0] = "poorva"
# print(len(names))

# #program 3
# #del names
# print("sarika" in names)

# #program 4
# # list allows duplicate values
# print(names)

# # loops
# cities = ["pune","mumbai","banglore","kolkata"]
# for x in range(len(cities)):
#     #print(x)
#     print(cities[x])

# for x in names:
#     print(x)

# i1 = 0
# while(i1 < len(cities)):
#     print(i1)
#     print(cities[i1])
#     i1 = i1 + 1

# methods 
# action and return type 
#           0       1        2       3
fruits = ["apple","mango","banana","orange"]
#insert()
fruits.insert(2,"chikoo")
print(fruits)

#append()
fruits.append('grapes')
print(fruits)

#remove()
# pop(1)
# pop()
# remove()
#               0            1              2        3
vegetables = ["brinjal","cauliflower","ladyfinger","tomato"]
# vegetables.pop()
# vegetables.pop(1)
# vegetables.remove('ladtfinger')


# program 3
#           0          1         2      3       4     5
country = ["india","srilanka","japan","cuba","india","USA"]
e = country.count('india')
print(e)
e = country.index('japan')
print(e)

country.reverse()
print(country)

country.sort()
print(country)

country.clear()
print(country)

numbers = [11,22,33]
# numbersB = numbers
# numbers[0] = 111
# print(numbers)
# print(numbersB)

numB = numbers.copy()
numB[0] = 0
print(numB)
print(numbers)