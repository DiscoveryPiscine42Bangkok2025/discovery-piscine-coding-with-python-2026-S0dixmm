#!/usr/bin/env python
# ใส่คำเข้าไป นับว่ามีกี่พารามิเตอร์ แล้วlenคำ
import sys

param_count = len(sys.argv) - 1

if param_count == 0:
    print("none")
else:
    print(f"parameters: {param_count}")

    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")
