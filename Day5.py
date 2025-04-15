info = [
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":26,
        "city":"sangamner",
        "skills":["javascript","cypress"]
        
    },
    {
        "firstName":"amol",
        "lastName":"rao",
        "age":35,
        "city":"pune",
        "skills":["sql","python","javascript"]

    },
    {
        "firstName":"snehalkamble",
        "lastName":"deshpande",
        "age":35,
        "city":"pune",
        "skills":["python","javascript","cypress","playwright"]

    },
        
    {
        "firstName":"aditi",
        "lastName":"kemkar",
        "age":27,
        "city":"Sinnar",
        "skills":["python","javascript","cypress","html","css"]

    }

]


# program 5

total  = 0
for person in info:
    total = total + person['age']

print(total/len(info))

#program 4
# firstname of person with city pune

# for person in info:
#     if person['city']  == "pune":
#         print(person['firstName'])
        

# program 3
# for person in info:
#     person['skills'].append('genAI')

# for person in info:
#     print(person['skills'])


# program 2
#print name and number of skills
# for person in info:
#     print(f'{person['firstName']}:{len(person['skills'])}')


# program 1
# list of firstname and lastName
# for person in info:
#     print(person['firstName'])
#     print(person.get('lastName'))