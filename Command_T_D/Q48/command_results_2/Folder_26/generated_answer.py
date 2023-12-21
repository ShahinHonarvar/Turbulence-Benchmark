
import bisect

def return_binary_or_hexa(tup):
    i = bisect.bisect_left(tup,68)
    j = bisect.bisect_right(tup,99)
    if (i != j):
        s = 0
        while i < j:
            s += tup[i]
            i += 1
        if s % 2:
            return '{:b}'.format(s)
        else:
            return '{:x}'.format(s)
    else:
        return ''
