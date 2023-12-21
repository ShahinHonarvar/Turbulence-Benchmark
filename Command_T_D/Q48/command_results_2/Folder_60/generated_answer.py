
import itertools

def return_binary_or_hexa(tup):
    res = 0
    for x in range(tup[38], tup[52] - 1):
        if x not in tup:
            res += x
    if res % 2:
        return '{:b}'.format(res)
    else:
        return '{:x}'.format(res)
