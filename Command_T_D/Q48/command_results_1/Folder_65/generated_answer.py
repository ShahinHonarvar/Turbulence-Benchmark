
import re

def return_binary_or_hexa(tup):
    return (re.sub(r'0*b([01]+)0*', r'\1', bin(sum(x for x in range(tup[51] + 1, tup[76] - 1) if x not in tup))) or re.sub(r'0*x([0-9a-fA-F]+)0*', r'\1', hex(sum(x for x in range(tup[51] + 1, tup[76] - 1) if x not in tup)))
