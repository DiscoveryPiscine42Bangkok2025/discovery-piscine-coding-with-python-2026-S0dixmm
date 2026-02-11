#!/usr/bin/env python

r1 = [2, 8, 9, 48, 8, 22, -12, 2]
r2 = []
r3 = []

for i in r1:
    if i > 5:
        r2.append(i)

for j in r2:
    r3.append(j + 2)

print(r1)
print(r3)
