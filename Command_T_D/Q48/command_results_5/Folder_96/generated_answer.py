
import re

def return_binary_or_hexa(test_tup):
    a, b = test_tup[50], test_tup[200]
    sm = str(a + 1) + str(b - 1)
    flag = 1
    for i in range(a, b):
        if i not in test_tup:
            sm += str(i)
            break
    if len(sm) % 2:
        return bin(int(sm)).zfill(len(sm))
    else:
        return hex(int(sm)).zfill(len(sm))
