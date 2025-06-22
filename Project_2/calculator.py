# Loop until the user enters a valid integer for num1
while True:
    try:
        num1 = int(input("Enter num1 : "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Please enter a valid integer for num1.")  # Prompt again if input is invalid

# Loop until the user enters a valid integer for num2
while True:
    try:
        num2 = int(input("Enter num2 : "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Please enter a valid integer for num2.")  # Prompt again if input is invalid

operator = str(input("Enter Operator (+,-,*,/,%,// or q to quit) : "))  #Declaring operator to perform operation on the numbers
if operator.lower() == "q":
    print("Exiting calculator.")
    exit()

def result():
    # Addition
    if operator == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    # Subtraction
    elif operator == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    # Multiplication
    elif operator == "*":
        result = num1 * num2
        print(f"{num1} x {num2} = {result}")
    # Division
    elif operator == "/":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    # Floor Division
    elif operator == "//":
        result = num1 // num2
        print(f"{num1} // {num2} = {result}")
    # Modulus
    elif operator == "%":
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
    else:
        print("Invalid Operator")
        
result()