try:
    a=int(input("enter your number:"))
    b=int(input("enter your number:"))
except ZeroDivisionError:
    print("cannot didvide by zero") #explaination of the error:- it occurs when a number is divided by zero, which is mathematically undefined.
else:
    print(a/b)

try:
    filename=input("enter the filename do you want :")
except FileNotFoundError:
    print("file not found") # explanation of the error:- it occurs when the specified file is not found.
else:
    print(filename)

try:
    num=int(input("enter your number:"))
except ValueError:
    print("invalid input") #explanation of the error:- it occurs when the input provided cannot be converted to an integer, such as entering a string instead of a number.
else:
    print(num)
