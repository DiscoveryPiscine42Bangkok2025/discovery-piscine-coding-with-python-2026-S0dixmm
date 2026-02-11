#!/usr/bin/env python

print("Enter a number")
num = int(input())
i = 0
cal = 0
for i in range (10):
    cal = (i*num)
    print(f"{i} x {num} = ",cal)
