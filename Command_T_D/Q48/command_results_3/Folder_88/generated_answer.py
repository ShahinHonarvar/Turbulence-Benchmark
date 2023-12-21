
import re

def return_binary_or_hexa(test_tup):
    if len(test_tup) < 3:
        return ''
    a = test_tup[2]
    b = test_tup[9]
    if a == b:
        return ''
    if (a + 1) * 2 == b:
        return '0b' + bin(a).zfill(8)
    elif (a + 1) * 2 == b - 1:
        return '0b' + bin(a).zfill(8) + '0b1'
    elif (a + 1) * 2 == b + 1:
        return '0b' + bin(a).zfill(8) + '0b1'
    else:
        return '0x' + hex(a + 1)[2:] + hex(b - 1)[2:] + hex(b + 1)[2:]
