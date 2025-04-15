# #        0  1  2
# lista = [11,22,33]
# #retrive
# print(lista[0])

# # update 

# lista[0] = 111
# print(lista)

# # in
# print(111 in lista)

# #length
# w = len(lista)
# print(w)

# #del lista


# # loop 
# #           0        1         2
# cities = ["pune","mumbai","bangalore"]
# # for - range()
# for x in range(len(cities)):
#     #print(x)
#     print(cities[x])

# # for 
# for x in cities:
#     print(x)

# # while
# i1 = 0
# while(i1 <= len(cities)):
#     print(cities[i1])
#     i1 = i1 + 1

#            0        1        2       3
fruits  = ["apple","mango","banana","grapes"]

# gym 
# action - excercise 
# return - health
fruits  = ["apple","mango","banana","grapes"]
e = fruits.append("papaya")
print(fruits)
print(e)

# program 2 
fruits  = ["apple","mango","banana","grapes"]
e1 = fruits.reverse()
print(e1)
print(fruits)

# program3
country = ["india","pakistan","srilanka","china"]
country2 = ["cuba","canada","USA"]
e2 = country.extend(country2)
print(e2)
print(country)

# program 4
country = ["india","pakistan","srilanka","china"]
country.clear()
print(country)

# program 5
#            0        1           2        3
country = ["india","pakistan","srilanka","china"]
country.remove("srilanka")
print(country)
country.pop(1)
country.pop()
print(country)
# remove(element) # pop(elementIndex) #pop()

# program 6
#              0          1        2
vegetable = ["tomatoe","potato","brinjal"]
vegetable.insert(2,"ladyfinger")
print(vegetable)

#program 7
vegetable = ["tomato","potato","brinjal","potato","tomato"]
e = vegetable.count('tomato')
print(e)

# program 8
names = ["mayuri","sarika","ram","sham","sachin","arna","chinmay"]
names.sort()
print(names)


d = [11,22,32]
e = d
e[0]= 111
print(d)
print(e)


names = ["chinmay","sarika","arna"]
# namesB = names
# namesB[2] = "arika"
# print(names)
# print(namesB)

namesC = names.copy()
namesC.append("rasika")
print(names)
print(namesC)

# 6:30 pm ist


n = [11,22,33,33,44,55,66,55,66,66,77]
count = 0

for x in range(len(n)):
    if n[x] == 66:
        count = count + 1
        print(x,n[x])
       

print(count)