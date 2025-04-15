# Generators 

def rangeFunction(x,y):
    for x in range(x,y):
        print(x)
rangeFunction(1,6)

# generator
# generator object

def mygen(x,y):
    while(x <= y):
        yield x
        x = x + 1
g = mygen(1,5) # generator ---> 1,2,3,4,5
print(g)
#e = next(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
for x in g:
    print(x)


def myGen():
    yield "A"
    yield "B"
    yield "C"

q = myGen()

print(next(q))
print(next(q))
print(next(q))


#[1,2,3,4,5,6] ---> memory
#   1
#   2
#   3
#   4
#   5
#   6