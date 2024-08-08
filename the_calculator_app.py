def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


    

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")




while(True):

    choice = (input("Enter your choice (1/2/3/4/5): "))

    if choice == '5':
        break
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    if choice == '1':
        print(f"{num1} + {num2} equals: {add(num1,num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} equals: {subtract(num1,num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} equals: {multiply(num1,num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} equals: {divide(num1,num2)}")
  
    else:
        print(f"{choice} is not a valid input. Please select (1, 2, 3, 4, 5)")

