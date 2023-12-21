
import sys

sys.setrecursionlimit(10**6)

def return_binary_or_hexa(tup):
    a, b = tup[25], tup[80]
    s = sum(x for x in range(a + 1, b) if x not in tup[25:80])
    if s % 2:
        return '{:b}'.format(s)
    else:
        return '{:x}'.format(s)
