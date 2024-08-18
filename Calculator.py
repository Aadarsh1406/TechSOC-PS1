""" This is a calculator that is used for basic stuff like add, subtract, multiply and divide. It is also used for trigonometric functions
like sin, cos and tan. It also has logarithm, exponent and solves quadratic equations. 
- Aadarsh S
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

def sine(x):
    sine_value = 0
    for n in range(10):
        sign = (-1)**n
        sine_value += sign * power(x, 2*n + 1) / factorial(2*n + 1)
    return sine_value

def cosine(x):
    cosine_value = 0
    for n in range(10):
        sign = (-1)**n
        cosine_value += sign * power(x, 2*n) / factorial(2*n)
    return cosine_value

def tangent(x):
    return sine(x) / cosine(x)

def log(x):
    if x <= 0:
        return "Logarithm undefined for non-positive numbers."
    
    if x == 1:
        return 0
    
    n = 0
    while x > 2:
        x /= 2.718281828459045  # Dividing by e to bring it closer to 1
        n += 1
    
    log_approx = 0
    y = (x - 1) / (x + 1)
    y_squared = y * y
    
    for i in range(100):
        log_approx += (1 / (2 * i + 1)) * y
        y *= y_squared

    return 2 * log_approx + n

def square_root(x):
    return x**0.5

def quadratic(a,b,c):
    """Function to solve a quadratic equation ax^2 + bx + c = 0."""

    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root1 = (-b + square_root(discriminant)) / (2 * a)
        root2 = (-b - square_root(discriminant)) / (2 * a)
        return root1, root2
    
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root
    
    else:
        real_part = -b / (2 * a)
        imaginary_part = square_root(-discriminant) / (2 * a)
        return (real_part, imaginary_part), (real_part, -imaginary_part)

def exponent(a,b):
    return a**b

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sine")
    print("6. Cosine")
    print("7. Tangent")
    print("8. Logarithm")
    print("9. Quadratic Equation")
    print("10. Exponent")
    
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    
    elif choice in ['5', '6', '7']:
        angle = float(input("Enter the angle in radians: "))
        
        if choice == '5':
            print(f"sine({angle}) = {sine(angle)}")
        elif choice == '6':
            print(f"cosine({angle}) = {cosine(angle)}")
        elif choice == '7':
            print(f"tangent({angle}) = {tangent(angle)}")
    
    elif choice == '8':
        num = float(input("Enter the number: "))
        print(f"log{num} = {log(num)}")

    elif choice == '9':
        x = float(input("Enter the coeffecient of x^2 (a): "))
        y = float(input("Enter the coeffecient of x (b): "))
        z = float(input("Enter the constant term of the Quadratic Equation (c): "))
        print("The roots of the quadratic quation are: ", quadratic(x,y,z))

    elif choice == '10':
        x = float(input("Enter the number: "))
        y = float(input("Enter the exponent of that number: "))
        print("The required answer is: ", exponent(x,y))
    
    else:
        print("Invalid Input")
    
    global repeat
    repeat = input("Do you want to do some other operation (Y/N): ")

# Run the calculator
calculator()

while repeat == 'Y':
    calculator()

else:
    print("Thank You")