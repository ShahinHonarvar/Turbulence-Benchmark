
import re

def return_binary_or_hexa(tup):
    a, b = tup[77], tup[84]
    if a == b:
        return ''
    s = str(a + 1) + '+' + str(b - 1)
    if s[0] == '0':
        s = re.sub(r'0+', '', s)
    return s[1:-1] + 'b' if len(s) % 2 == 1 else '0x' + s[1:-1]
