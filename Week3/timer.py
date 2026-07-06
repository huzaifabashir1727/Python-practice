import time

list = [2,4,6,8,10]

def decorator(task):
    def timer():
        Starttime = time.time()
        Functioncall = task()
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
def Poppingmethod():
    list.pop()
    print(list)
    
@decorator
def display():
    for num in list:
        print(num)
        
increment()
Poppingmethod()
display()