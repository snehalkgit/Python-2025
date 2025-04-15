
fn = "Snehal"
e = fn.upper()
print(e)

ln = 'sonu'
f = ln.lower()
print(f)

mn = "kamble"
m = mn.capitalize()
print(m)

city = "PUNE"
h = city.isupper()
print(h)

city2 = "Goa"
h = city2.islower()
print(h)

info = 'I Am Learning js'
h = info.istitle()
print(h)


strOne = "12321312"
g = strOne.isnumeric()
print(g)

strTwo = "aaa"
f = strOne.isalpha()
print(f)


strThree = "a2234324324" #only alphabets , only numbers 
g = strThree.isalnum()
print(g)




country = "India"
n = country.startswith('i')
e = country.startswith('india')
print(n)
print(e)

a1 = country.endswith('a')
a2 = country.endswith('ia')
print(a1)
print(a2)


print(" ".isspace())
print(len(" "))