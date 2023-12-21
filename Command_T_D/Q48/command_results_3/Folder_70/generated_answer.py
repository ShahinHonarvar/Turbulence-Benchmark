
import sys

def return_binary_or_hexa(tup):
    a, b = tup[43], tup[70]
    return ("0b" + bin(a + 1 + sum(x for x in range(a + 2, b, 2)) if x not in tup[43:70]))) or ("0x" + hex(a + 1 + sum(x for x in range(a + 2, b, 2)) if x not in tup[43:70])))
