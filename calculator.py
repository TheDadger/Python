import math

def add(a,b):
    try:
        return a + b
    except Exception as e:
        print(f"{e}")

def subtract(a,b):
    try:
        return a - b
    except Exception as e:
        print(f"{e}")

def multiply(a,b):
    try:
        return a * b
    except Exception as e:
        print(f"{e}")

def divide(a,b):
    #I learned exception handling from here and got introduced with try except, raise finally etc.
    try:
        return a / b
    except Exception as e:
        print(f"{e}")
    # finally:
    #     return "Error"
    #any error will be printed and 0 will be returned

def main():
    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    op=input("Enter operation (+, -, *, /): ")
    # wow match case is new in python 3.10
    match op:
        case '+':
            print(f"Result: {add(a,b)}")
        case '-':
            print(f"Result: {subtract(a,b)}")
        case '*':
            print(f"Result: {multiply(a,b)}")
        case '/':
            print(f"Result: {divide(a,b)}")
        case _:
            print("Invalid operation")
        
main()