my_dict = {
    "name":"sonu",
    "lastName":"kamble",
    "age":12,
    "skills":["python","css","java"]
}
print(type(my_dict))


# program 2
my_dict2 = {
    "name":"aishwarya",
    "lastName":"kallmt",
    "age":12,
    "skills":["python","css","java"]
}

# retrive 
print(my_dict2['name'])
e = my_dict2.get('age')
print(e)


# program 3
# update
my_dict3 = {
    "name":"harsha",
    "lastName":"pande",
    "age":12,
    "skills":["python","css","java"],
    "age":35
}
my_dict3['name'] = "tanmay"
print(my_dict3)
# does dictionary allows to store duplicate keys?
my_dict3.update({"lastName":"dani"})
print(my_dict3)

# program 4
my_dict4 = {
    "name":"kavita",
    "lastName":"pande",
    "age":12,
    "skills":["python","css","java"],

}
my_dict4['language'] = "marathi"
my_dict4.update({"city":"pune"})
print(my_dict4)

# program 5
my_dict5 = {
    "name":"kalu",
    "lastName":"prasad",
    "age":12,
    "skills":["python","css","java"],

}
# particular key exist or not ??
print("name" in my_dict5)
print("city" not in my_dict5)
# total number of keys and values 
q1 = len(my_dict5)
print(q1)

# program 6
my_dict6 = {
    "name":"chammu",
    "lastName":"thool",
    "age":12,
    "skills":["python","css","java"],

}

# 3 ways 
my_dict6.popitem()
print(my_dict6)
my_dict6.pop('age')
print(my_dict6)
#del my_dict6
del my_dict6['name']

# program 7
# does dictionary stores value by index
# my_dict6 = {
#     "name":"harsha",
#     "lastName":"kale",
#     "age":12,
#     "skills":["python","css","java"],
# }
# print(my_dict6[0])

# program 8

my_dict6 = {
    "name":"snehal",
    "lastName":"kadu",
    "age":12,
    "skills":["python","css","java"],
}
for x in my_dict6.keys():
    print(x)

for x in my_dict6.values():
    print(x)

for k,v in my_dict6.items():
    print(k,v)


# program 9
my_dict6 = {
    "name":"snehal",
    "lastName":"kamble",
    "age":12,
    "skills":["python","css","java"],
}
# my_dict6.clear()
# print(my_dict6)

e = dict.fromkeys(["admin","customer","manager"])
print(e)


# program 10
vehicle = {
    "color":"red",
    "type":"sedane"
}
f =  vehicle.setdefault('regNo','123')
print(f)
print(vehicle)


vehicle = {
    "color":"red",
    "type":"sedane"
}
# vehicle2 = vehicle
# vehicle['color'] = "blue"
# print(vehicle)
# print(vehicle2)

vehicle2= vehicle.copy()
vehicle2['color'] = "green"
print(vehicle)
print(vehicle2)

# program 11
vehicle = {
    "color":"red",
    "type":"sedane"
}

for key in vehicle:
    print(key,vehicle[key])


#           0        1      2        3
names = ["chinmay","ram","sarika","satish"]
print(names[0])

#
names[0] = 'tanmay'
print(names)
# allows duplicate value
#          0        1       2        3        4
fruits = ["apple","mango","banana","orange","mango"]
print(fruits)
print("Apple" in fruits)
print(len(fruits))

numbers = [11,22,33,44]
print(len(numbers))