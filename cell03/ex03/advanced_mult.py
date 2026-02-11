#!/usr/bin/env python

i = 0
while i <= 10:
    j = 0
    print(f"Table de {i}:", end=" ")
    while j <= 10:
        print(i * j, end="")
        if j < 10:
            print(" ", end="")
        j += 1
    print()
    i += 1













# i = 0
# j = 0
# k = 0
# while (i <= 11):
#     print(f"Table de {i}: ")
#     i+=1
#     while (j <= 10):
#         j+=1
#         while (k <= 10):
#             print (k+i)
#             k+=1