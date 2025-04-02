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

def calculator():
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to exit the program")

        user_input = input("Choose an operation: ").lower()

        if user_input == "quit":
            print("Goodbye!")
            break
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if user_input == "add":
                print(f"The result is: {add(num1, num2)}")
            elif user_input == "subtract":
                print(f"The result is: {subtract(num1, num2)}")
            elif user_input == "multiply":
                print(f"The result is: {multiply(num1, num2)}")
            elif user_input == "divide":
                print(f"The result is: {divide(num1, num2)}")
        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calculator()
