my_dict = {
    "name":"aditi",
    "lastName":"katwe",
    "age":12
    
}
print(my_dict)
print(type(my_dict))

# program 2
# create / retrive /update/delete

my_dict = {
    "name":"samiksha ",
    "lastName":"pande",
    "age":12
    
}
print(len(my_dict))
# does dictionary stores the value by index ?
#print(my_dict[0])

# retrive 
info = {
    "name":"harsha",
    "age":35,
    "city":"newyork"
}
print(info['name'])
e = info.get('name')
print(e)
print(info['age'])
f =info.get('age')
print(f)

# program 2
# update and add and search
info = {
    "name":"snehal",
    "age":35,
    "city":"newyork"
}
print(type(info))
print(info['name'])
# update
info['name'] = "samay"
# add
info['language'] = "marathi"
print(info)
print(info)
#search
print("name" in info)
print("fname" in info)
# program 3

info = {
    "name":"sonu",
    "age":35,
    "city":"newyork"
}

info.popitem()
print(info)
# info.pop('age')
# print(info)
#del info
#print(info)
del info['age']
print(info)
info.clear()
print(info)

#program4
# does dictionalry allows to store duplicate value 

vehicle = {
    "color":"red",
    "type":"suv",
    
}

for x in vehicle:
    print(x,vehicle[x])

for x in vehicle.keys():
    print(x)
for x in vehicle.values():
    print(x)
for x in vehicle.items():
    print(x)



# print(vehicle)
# print(vehicle.keys())
# print(vehicle.values())
# print(vehicle.items())