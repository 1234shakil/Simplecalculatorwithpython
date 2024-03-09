print("THIS IS A SIMPLE CALCULATOR")
print("+ this name is Addition (Enter name this :ADD)")
print("- this name is Subtraction (Enter name this : SUB)")
print("* this name is Multiplication (Enter name this : MUL)")
print("/ this name is Division (Enter name this : DIVI)")
print("% this name is percentage (Enter name this : PRECNT)")

try:
    Operator = input("Enter Calculation Name :")

    if Operator == "ADD" :
        Num1 = int(input("Enter 1st addition number(Only Number) :"))
        Num2 = int(input("Enter 2st addition number(Only Number) :"))
        ans = Num1 + Num2
        print(f"Your Answare is {ans}")
    elif Operator == "SUB" :
        Num1 = int(input("Enter 1st Subtraction number(Only Number) :"))
        Num2 = int(input("Enter 2st Subtraction number(Only Number) :"))
        ans = Num1 - Num2
        print(f"Your Answare is {ans}")
    elif Operator == "MUL" :
        Num1 = int(input("Enter 1st Multiplication number(Only Number) :"))
        Num2 = int(input("Enter 2st Multiplication number(Only Number) :"))
        ans = Num1 * Num2
        print(f"Your Answare is {ans}")
    elif Operator == "DIVI" :
        Num1 = float(input("Enter 1st Division number(Only Number) :"))
        Num2 = float(input("Enter 2st Division number(Only Number) :"))
        ans = Num1 / Num2
        print(f"Your Answare is {ans}")
    elif Operator == "PRECNT" :
        Num1 = float(input("Enter 1st percentage number is your Main number(Only Number) :"))
        Num2 = float(input("Enter 2st percentage number(Only Number) :"))
        Num3 = Num1 * (Num2 / 100)
        ans = Num1 - Num3
        print(f"Your Answare is {ans} . will be removed from main number {Num3}")
    else:print("Your calculation name is Invalid")
except:
    print("Anything is Error in code, Check your code")