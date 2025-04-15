
# List

# names = ["chinmay","sarika","sarika",'shraddha',"sachin","sameer"]
# print(names[0])
# names[0] = "ram"
# print(names)
# print("ram" in names)
# print("ram" not in names)
# print(names)
# print(len(names))
# names[0]= "hemant"
# print(names)
# del names

# #           0       1         2         3
# cities = ["pune","mumbai","banglore","chennai"]
# for x in range(len(cities)):
#     #print(x)
#     print(cities[x])

# for item  in cities:
#     print(item)

# i1 = 0 
# while(i1 < len(cities)):
#     #print(i1)
#     print(cities[i1])
#     i1 = i1 + 1



# program 1 

#           0       1         2       3
fruits = ["apple","mango","banana","orange"]
#           -4      -3         -2        -1
print(fruits)
fruits.append("papaya")
print(fruits)


# pop()  by default takes -1 as index
fruits.pop()
print(fruits)
fruits.pop(2)
fruits.remove("apple")
print(fruits)

# append()
# pop()
# pop(2)
# remove(element)

# program 2
#            0         1          2         3       4       5
country = ["india","pakistan","srilanka","japan","tokiyo","india"]
e = country.count("india")
print(e)
country.clear()
print(country)

# program 3
numbers = [11,22,33]
numbersB  = [44,55]
#numbers.extend(numbersB)
numbersB.extend(numbers)
print(numbers)
print(numbersB)


# program 5
#               0          1        2          3
vegetables = ["cabbage","tomato","potato","ladyfinger"]
# vegetables.insert(3,"onion")
# print(vegetables)

# f = vegetables.index("potato")
# print(f)

vegetables.reverse()
print(vegetables)

vegetables.sort()
print(vegetables)