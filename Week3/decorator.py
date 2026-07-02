def decorator(func):
    def wrapper():
        print("Before the function runs")
        result = func()
        print("After the function runs")
        return result
    
    return wrapper

@decorator
def say_hello():
    print("Hello!")
    
say_hello()

# *arg
def add(*args):
    return sum(args)

add(1, 2, 3)

def sum(nums):
    result = 0
    for num in nums:
        result = result + num
    
    return result
        
sum([1,2,3,4,5])

# **kwargs

def users(**kwargs):
    user = []
    for key,value in kwargs.items():
        user.append(f"{key}: {value}")
    
    print(user)

users(Name="Huzaifa", Age=22, Semester="7th")

#practice
Uppercaselist = []
def decorator(func):
    def wrapper(*args):
        for string in args:
            Touppercase = string.upper()
            func(Touppercase)
            
        print(Uppercaselist)
    
    return wrapper

@decorator
def Uppercase(string):
    Uppercaselist.append(string)
    
Uppercase("huzaifa","hello","cat","totowolf")