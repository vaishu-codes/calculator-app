def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add (जोड़ना)")
        print("2. Subtract (घटाना)")
        print("3. Multiply (गुणा)")
        print("4. Divide (भाग)")
        print("5. Exit (बाहर निकलें)")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting calculator... Goodbye Vaishnavi!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error! Please enter valid numbers.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice! Please select again.")

# Run calculator
calculator()
