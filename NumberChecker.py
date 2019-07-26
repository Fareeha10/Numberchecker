#	Write a Python program to check if a number is positive, negative or zero
num = int(input("Enter number to see if it is positive, negative or zero :"))
if num == 0:
    print("Number is zero")
elif num > 0:
    print("Number is positive")
else:
    print("Number is negative")