

# Addition and substraction inside the methods

def add():
    a = 20
    b = 30
    total = a + b
    print("Total is", total)

def sub():
    a = 20
    b = 30
    total = a - b
    print("Total is", total)

def multi():
    a = 20
    b = 30
    total = a * b
    print("Total is", total)

def div():
    a = 20
    b = 30
    if b != 0:  # Check for division by zero
        total = a / b
        print("Total is", total)
    else:
        print("Error: Division by zero is not allowed.")

# Get user input
s1 = input("Enter the operation (addition, subtraction, multiplication, division): ").strip().lower()

# Check user input and call the appropriate function
if s1 == "addition":
    add()
elif s1 == "subtraction":
    sub()
elif s1 == "multiplication":
    multi()
elif s1 == "division":
    div()
else:
    print("Please check the spelling for input.")