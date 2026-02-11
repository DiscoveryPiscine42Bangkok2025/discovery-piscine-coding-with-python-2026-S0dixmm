#!/usr/bin/env python

import sys

sum = len(sys.argv)
if (sum == 1):
    print("None")
elif (sum > 1):
    print(sys.argv[1]) 