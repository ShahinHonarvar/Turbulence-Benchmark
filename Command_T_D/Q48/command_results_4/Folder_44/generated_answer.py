
import re

def return_binary_or_hexa(test_list):
    a, b = test_list[36], test_list[52]
    x = sum(list(range(a + 1, b - 1)))
    if x % 2 == 0:
        return hex(x)
    else:
        return re.sub(r'0x', '', hex(x))
