
import re

def return_binary_or_hexa(tup):
    s = sum(x for x in range(tup[2]+1,tup[7]-1))
    if s%2:
        return re.sub(r'([01]0+)',r'\1',bin(s)[2:])
    else:
        return re.sub(r'([0-9A-F]+)',r'\1',hex(s))
