def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("This is a simple calculator module.")
    print("Use the functions add, subtract, multiply, and divide to perform calculations.")
    print("Add: ", add(5, 3))
    print("Subtract: ", subtract(5, 3))
    print("Multiply: ", multiply(5, 3))
    print("Divide: ", divide(5, 3))
    print("Divide by zero test: ", divide(5, 0))  # This will raise an exception