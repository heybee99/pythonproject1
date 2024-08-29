import math
import cmath

def home():

    print("""
                    SIMPLE CALCULATOR
        What do you want to perforrm? 
        1. Addition
        2. Subtraction 
        3. Multiplication
        4. Division
        5. Cos
        6. Sin
        7. Tan
        8. square power
        9. pi
        0. log
        11. Square root
        """)
    try:
        option = int(input("Operator: ") )
    except ValueError:
        print("Enter a number")
    else:
        if option == "1":
            add()
        elif option == "2":
            sub()
        elif option == "3":
            multiply()
        elif option == "4":
            divide()
        elif option == "5":
            cos() 
        elif option == "6":
            sin()
        elif option == "7":
            tan() 
        elif option == "8":
            power()
        elif option == "9": 
            pi()
        elif option == "0":
            log()
        elif option == "11":
            log()
        else:
            print("Invalid")

def add():
    val1 = float(input("Value 1: "))
    val2 = float(input("Value 2: "))
    result = (val1 + val2)
    print(f"Answer = {result}") 
def sub():
    val1 = float(input("Value 1: "))
    val2 = float(input("Value 2: "))
    result = (val1 - val2)
    print(f"Answer = {result}")
def multiply():
    val1 = float(input("Value 1: "))
    val2 = float(input("Value 2: "))
    result = (val1 * val2)
    print(f"Answer = {result}") 
def divide():
    val1 = float(input("Value 1: "))
    val2 = float(input("Value 2: "))
    result = (val1 / val2)
    print(f"Answer = {result}") 
def cos():
    val1 = float(input("Value 1: "))
    result = cmath.cos(val1)
    print(f"Answer = {result}")
def sin():
    val1 = float(input("Value 1: "))
    result = cmath.sin(val1) 
    print(f"Answer = {result}")
def tan():
    val1 = float(input("Value 1: "))
    result = cmath.tan(val1)
    print(f"Answer = {result}")
def power():
    val1 = float(input("Value 1: "))
    result = val1**2 
    print(f"Answer = {result}")
def pi():
    val1 = float(input("Value 1: "))
    result = cmath.pi(val1)
    print(f"Answer = {result}")
def log():
    val1 = float(input("Value 1: "))
    result = cmath.log10(val1) 
    print(f"Answer = {result}")
def root():
    val1 = float(input("Value 1: "))
    result = math.sqrt(val1) 
    print(f"Answer = {result}")  

home()