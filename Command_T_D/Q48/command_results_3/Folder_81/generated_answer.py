
import re

def return_binary_or_hexa(tup):
    a, b = tup[10], tup[100]
    if a <= b - 1:
        return '0b' + str(sum(x for x in range(a + 1, b - 1) if x not in tup[10:100]))
    else:
        return '0x' + re.sub(r'([A-F]+)([A-F]?)', r'\1\2', str(sum(x for x in range(a + 1, b - 1) if x not in tup[10:100])))
