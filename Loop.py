# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for and while 
#range(start,end,steps)

# program 1
# start - 0
# end - (not included) 5
# stepSize - 1
for x in range(5):
    print(x)


# program 2
# start  - 1
# end - 6
# stepSize - 1
for x in range(1,6):
    print(x)


# program 3
# print hello 3 times 
for x in range(3):
    print("hello")

# program - 4
# table of 2
for x in range(1,11):
    print(x * 2)

# program 5
# 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
for x in range(2,21,2):
    print(x)

# program 6
for x in range(3,31,3):
    print(x)

# program 7
# print 5 to 1
for x in range(5,0,-1):
    print(x)


# program 8
# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)

# program 9
# table of 5 in reverse
for x in range(50,4,-5):
    print(x)

# program 10
# break - statement
for x in range(1,6): # 2 # 3
    if x == 3:
        break
    print(x) # 1 # 2

for x in range(20,1,-2):
    if x == 14:
        break
    print(x)

for x in range(10,1,-1):
    if x == 5:
        break
    print(x)

# continue with for loop

for x in range(1,6): # 2 # 3 # 4 # 5
    if x == 3:
        continue
    print(x) # 1 # 2 # 4 # 5