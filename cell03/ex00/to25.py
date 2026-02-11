#!/usr/bin/env python

num = int(input())
if (num > 25):
    print("error")

elif (num <= 25):
    while (num != 26):
        print("Inside the loop, my variable is ",num)
        num += 1
