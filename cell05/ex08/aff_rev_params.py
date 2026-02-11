#!/usr/bin/env python
# ถ้าน้อยกว่า3 0 จะnone แต่ถ้ามากกว่าหรือเท่ากับ 3 จะแสดงค่าออกมาแบบเรียงกลับหลัง
import sys

if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1
