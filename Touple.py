a = 10
print(a)
print(type(a))

city = ["pune","mumbai","banglore"]
print(city)
print(type(city))

d = {
    "firstName":'chinmay',
    "lastName":"deshpande"
}
print(d)
print(type(d))

# how to define tuple 

a = 10
print(a)
print(type(a))

a = 10,
print(a)
print(type(a))

b = 10,2
print(b)
print(type(b))

c = (11,22,33,44,55)
print(c)
print(type(c))

d = ("chinmay","deshpande",34,True)
print(d)
print(type(d))

# does tuple stores the value by index 
d = (11,22,33)
print(d[0])

# immutable 
#d[0] = 23
d = (22,33,44,55)
print(d)
print(type(d))

# can we store duplicate values inside tuple - yes
e = (11,22,33,44,33)
print(e)

# cannot delete single element 
# del e[0]
# print(e)


# loop 
# for loop using range()
#    0  1  2  3
g = (11,22,33,44)
print(type(g))
print(len(g))


# for loop without range() / for loop
for x in range(4):
    #print(x)
    print(g[x])

for item in g:
    print(item)

# while loop
#           0       1         2        3
cities = ("pune","mumbai","kolkata","chennia")
for x in range(len(cities)):
    #print(x)
    print(cities[x])

r1 = 0
while r1 < len(cities):
    #print(r1)
    print(cities[r1])
    r1 = r1 + 1

# particular element aviable in tuple 
a = (100,22,33)
print(100 in a)
print(1000 not in a)
print(90 in a)

# unpacking of tuple
country = ('india',"srilanka","pakistan","japan")
(a,b,c,d)=country
print(a)
print(b)
print(c)
print(d)
#            0          1         2        3        4
country = ('india',"srilanka","pakistan","japan","india")
e = country.count('india')
print(e)
e1 = country.index("india")
print(e1)
e2 = country.index("india",2)
print(e2)