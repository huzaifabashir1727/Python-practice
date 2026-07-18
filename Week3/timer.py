import time
from functools import wraps

list = [2,4,6,8,10]

def decorator(task):
    # @wraps(task)
    def timer(*args):
        Starttime = time.time()
        Functioncall = task(*args)
        end = time.time()
        
        Totaltime = end - Starttime
        print(f"Total time: {Totaltime:.4f} seconds")
        
        return Functioncall
    
    return timer

@decorator
def increment():
    for i in range(len(list)):
        list[i] = list[i] + 2
        
    print(list)

@decorator
def popping_method():
    list.pop()
    print(list)
    
@decorator
def display():
    for num in list:
        print(num)
        
@decorator
def add_item(*item):
    list.extend(item)
    print(list)

increment()
popping_method()
display()
add_item(100,32)

print(add_item.__name__)
print(add_item.__doc__) 