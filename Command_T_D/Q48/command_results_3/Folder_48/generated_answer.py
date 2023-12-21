
import re

def return_binary_or_hexa(tup):
    a, b = tup[933], tup[996]
    s = sum(i for i in range(a + 1, b - 1) if i not in tup[933:996])
    return (re.sub(r"0b\d+", r"b\1", f"{s:b}"),
