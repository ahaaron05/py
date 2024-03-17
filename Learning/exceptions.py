"""
print("Enter two numbers, and I'll divide them...")
print("Enter 'q' to quit...")

while True:
    num1 = input("First number: ")
    if num1 == 'q':
        break
    num2 = input("Second number: ")
    if num2 == 'q':
        break
    try:
        answer = float(num1) / float(num2)
    except ZeroDivisionError:
        print("Couldn't divide by zero")
    else:
        print(f"The quotient is: {answer}")
        break
"""

file_path = "blank.txt"

try:
    with open(file_path) as f:
        contents = f.read()
except FileNotFoundError:
    print("FILE COULD NOT BE OPENED")
else:
    print(contents)