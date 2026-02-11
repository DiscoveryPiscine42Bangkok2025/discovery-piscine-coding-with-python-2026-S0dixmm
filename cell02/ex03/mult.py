#!/usr/bin/env python
print("Enter your first number : ")
num1 = int(input())
print("Enter your second number : ")
num2 = int(input())

cal = (num1*num2)

print(f"{num1} x {num2} = {cal}")

if (cal < 0):
    print("This number is negative.")

elif (cal > 0):
    print("This number is positive")

else:
    print("This number is both positive and negative.")
