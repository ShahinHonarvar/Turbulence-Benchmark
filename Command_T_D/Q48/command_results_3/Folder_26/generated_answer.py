
import itertools

def return_binary_or_hexa(tup):
    a, b = tup[68], tup[99]
    odds = itertools.accumulate(range(a + 1, b - 1))
    if len(odds) % 2 == 1:
        return ''.join(str(i) for i in odds)
    else:
        return hex(sum(odds))
