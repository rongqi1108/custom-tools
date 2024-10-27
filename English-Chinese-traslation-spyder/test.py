import re

string = "001.sdgsd.mp4"
match = re.search(r'\.(.*?)\.', string)
if match:
    middle_part = match.group(1)
    print(middle_part)
else:
    print("未找到两个小数点中间的内容")