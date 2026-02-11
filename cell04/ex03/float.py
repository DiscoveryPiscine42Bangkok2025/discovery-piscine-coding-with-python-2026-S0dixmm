#!/usr/bin/env python

num = input("Give me a Number : ")

check = num.isdigit()

if (check == True):
    print("This number is an integer.")

else :
    print("This number is a decimal.")