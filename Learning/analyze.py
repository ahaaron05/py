"""
file_path = "Learning/blank.txt"

try:
    with open(file_path) as f:
        words = f.read()
except FileNotFoundError:
    pass
else:
    print(len(words.split()))
"""

""" print("Enter two numbers...")
print("Press 'q' to quit...")

while True:
    num1 = input("First: ")
    if num1 == 'q':
        break
    num2 = input("Second: ")
    if num2 == 'q':
        break
    
    try:
        solution = int(num1) + int(num2)
    except ValueError:
        print("You entered a string")
    else:
        print(solution)
        break """

fp = "Learning/the_reaping.txt"

try:
    with open(fp, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Couldn't read file!")
else:
    print(contents.count("captain"))