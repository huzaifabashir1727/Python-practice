users = [{"name" : "Huzaifa", "roll_no" : 1727, "age" : 20},
         {"name" : "Ali", "roll_no" : 1728, "age" : 21},
         {"name" : "Ahmed", "roll_no" : 1729, "age" : 22},
         {"name" : "Hassan", "roll_no" : 1730, "age" : 23},
         {"name" : "Haris", "roll_no" : 1731, "age" : 24}]

def generator():
    for user in users:
        yield user

gen = generator()

def inputs():
    try:
        print(next(gen))
    except StopIteration:
        return  "No data available."

    while True:
        option = input("Want another Data (yes/no): ")

        if option == "no":
            break
        if option != "yes":
            print("Wrong input")
            continue
    
        try:
            print(next(gen))
        except StopIteration:
            print("No more data left.")
            break

inputs()