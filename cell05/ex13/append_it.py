#!/usr/bin/env python
# ถ้าไม่มี ism เติม ism

import sys

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(word + "ism")
