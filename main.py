def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
def modulo(x, y):
    
    return x % y

def main():
    # Hardcoded inputs for Jenkins
    num1 = 10
    num2 = 5
    choice = '4'  # Change this to '2', '3', or '4' to test other operations

    print(f"Running calculator with values: {num1}, {num2}")
    print("Operation choice:", choice)

    if choice == '1':
        print("Addition Result:", add(num1, num2))
    elif choice == '2':
        print("Subtraction Result:", subtract(num1, num2))
    elif choice == '3':
        print("Multiplication Result:", multiply(num1, num2))
    elif choice == '4':
        print("Division Result:", divide(num1, num2))
    elif choice == '5':
        print("Modulo Result:", modulo(num1, num2))    
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
