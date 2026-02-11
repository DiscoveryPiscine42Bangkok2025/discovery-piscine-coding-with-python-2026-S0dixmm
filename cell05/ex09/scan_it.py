#!/usr/bin/env python
# รับค่า 2 ค่า อันแรก คีย์อัน 2 ประโยคยาวๆๆ ว่าเจอกี่คำ
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]

    count = text.count(keyword)

    if count == 0:
        print("none")
    else:
        print(count)
