users = [{"name" : "Huzaifa", "roll_no" : 1727, "age" : 20},
         {"name" : "Ali", "roll_no" : 1728, "age" : 21},
         {"name" : "Ahmed", "roll_no" : 1729, "age" : 22}]

def generator():
    for user in users:
        yield user
        
gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))