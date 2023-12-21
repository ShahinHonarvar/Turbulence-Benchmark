
import re

def return_binary_or_hexa(tup):
    return re.sub(r'0b[01]+$|0o[0-7]+$|0x[0-9a-fA-F]+$', '', str(sum(range(tup[20] + 1, tup[200] - 1, 2)))))
