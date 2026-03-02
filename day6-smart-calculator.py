import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def square_root(a):
    if a < 0:
        return "Cannot take square root of negative number"
    return math.sqrt(a)


def main():
    while True:
        print("\n=== Smart Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == "8":
            print("Goodbye!")
            break

        try:
            if choice == "7":
                a = float(input("Enter number: "))
                print("Result:", square_root(a))
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", add(a, b))
                elif choice == "2":
                    print("Result:", subtract(a, b))
                elif choice == "3":
                    print("Result:", multiply(a, b))
                elif choice == "4":
                    print("Result:", divide(a, b))
                elif choice == "5":
                    print("Result:", power(a, b))
                elif choice == "6":
                    print("Result:", modulus(a, b))
                else:
                    print("Invalid choice.")

        except:
            print("Invalid input. Please enter numbers only.")

main()
