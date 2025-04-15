# program 1

#intialization
# while(condition){
    # statements
    # increment/decrement
#}
i1 = 1
while(i1 <= 3):
    print(i1) # 1 # 2 # 3
    i1 = i1 + 1 # 2 #3 #4
    
# program 2
# print hello 3 types 

i2 = 1
while(i2 <= 3):
    print("hello") # hello # hello # hello
    i2 = i2 + 1 # 2 # 3 # 4
    
#program 3
i3 = 1
while(i3 <= 5):
    print(i3) # 1 #2 #3 #4 #5
    i3 = i3 + 1 #2 #3 #4 #5 #6

#program 4
i4 = 1
while(i4 <= 10):
    print(i4 * 2)
    i4 = i4 + 1

# program 5
i5  = 2
while(i5 <= 20):
    print(i5)
    i5 = i5 + 2

# program 6
# table of three in reverse
i5 = 30
while(i5 >= 3):
    print(i5) # 30 # 27 -------------------3
    i5 = i5 - 3 # 27 ----------------0

#program 7
# table of 5 in reverse
i6 = 50
while(i6 >= 5):
    print(i6)
    i6 = i6 - 5
    
#program 8
i7 = 1
while(i7 <= 5):
    if i7 == 3:
        break
    print(i7)
    i7 = i7 + 1
    
i8  = 1
while(i8 <= 5):
    print(i8)  #1 #2 #3
    if i8 == 3:
        break
    i8 = i8 + 1 #2 #3

# program 4
i9 = 1
while(i9 <= 5):
    if i9 == 3:
        i9 = i9 + 1 #4
        continue
    print(i9)#1 #2 #4 #5
    i9 = i9 + 1 #2 #3 #5 #6