result = 0
operator = ""
first = True

def calculator(number, operator):
    global result,first

    if operator == "+":
        result += number
    elif operator == "-":
        result -= number
    elif operator == "*":
        if first:
            result = 1
        result *= number
    elif operator == "/":
        if first:
            result = number
        else:
            result /= number

    first = False

def inputs():
    global operator,result,first
    
    while True :
        try:
            number = int(input("Enter number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        new_operator = input("Enter operator: ")
        
        if new_operator not in ["+", "-", "*", "/", "="]:
            print("Invalid operator! Please enter +, -, *, / or =.")
            continue
        
        if first and new_operator == "=":
            print("First operator should not be =")
            continue
        
        if new_operator == "=":
            calculator(number,operator)
            print(f"Result: {result}")
            break
        else:
            if first :
                calculator(number,new_operator)
            else :
                calculator(number,operator)
            operator = new_operator
        
inputs()