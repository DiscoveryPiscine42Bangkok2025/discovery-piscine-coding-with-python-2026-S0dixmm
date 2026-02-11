#!/usr/bin/env python

r1 = [2, 8, 9, 48, 8, 22, -12, 2]
seen = set()
result = []

for i in r1:
    if i not in seen:
        seen.add(i)
        result.append(i + 2)

print(r1)
print(result)
