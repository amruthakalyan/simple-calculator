def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error! Division by zero."

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter choice (1/2/3/4): "))  # Get user choice

    num1 = float(input("Enter first number: "))  # Get first number
    num2 = float(input("Enter second number: "))  # Get second number

    if choice == 1:
        print(f"Addition Result: {add(num1, num2)}")
    elif choice == 2:
        print(f"Subtraction Result: {subtract(num1, num2)}")
    elif choice == 3:
        print(f"Multiplication Result: {multiply(num1, num2)}")
    elif choice == 4:
        print(f"Division Result: {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
