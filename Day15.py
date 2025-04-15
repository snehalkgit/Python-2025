# Decorators 

# logging 
# Access control 
# Caching 
# Time execution

def greet():
    print('hello')
greet()

def outer():
    def inner():
        print('hello')
    inner()
outer()

def outer():
    def inner():
        print("hello")
    return inner
e = outer()
print(e)
e()



def decorator_function(original_function):
    def wrapper_function():
        print("Before function is called")
        original_function()
        print("after function is called")
    return wrapper_function

# e = decorator_function(say_hello)
# e()



@decorator_function
def say_hello():
    print("hello")
say_hello()


# program 2

# def add(*agrs):
#     print(agrs) # tuple
# add(1,23,4,5,6,7,8,9,9,5,6,7)

# def add(**kwargs):
#     print(kwargs) # tuple
# add(a=1,b=2)
    

def decorator(func):
    def wrapper(nm,*args,**kwargs):
        return func(nm,*args,**kwargs)
    return wrapper
  
@decorator
def greet(nm,*name,**kwargs):
    print(f'Hi {name}')
    print(kwargs)
    print(nm)

greet("hello",1,2,3,4,5,5,a=1,b=3)