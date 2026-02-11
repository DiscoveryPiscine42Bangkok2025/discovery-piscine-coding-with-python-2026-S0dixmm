#!/usr/bin/env python

import sys

sum = len(sys.argv)
if (sum == 2):
    result = sys.argv[1]
    result2 = result.upper()
    print(result2)
else:
    print("none")
