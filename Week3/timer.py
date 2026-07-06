import time

list = [2,4,6,8,10]

def decorator(task):
    def timer():
        Starttime = time.time()
        Functioncall = task()
        end = time.time()
        
        return Functioncall
    
    return timer

@decorator
def increment():
    for num in list:
        num = num + 2

@decorator
def Poppingmethod():
    list.pop()
    
