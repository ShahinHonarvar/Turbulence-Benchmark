import re
import heapq
def all_left_truncatable_prime(tup):
    x = tup[38]
    rex = re.compile('0*(?:\d)*')
    lst = []
    for i in range(2, x):
        m = rex.match(str(i))
        if m:
            if m.group():
                j = int(m.group())
            else:
                j = 0
            if all(str(i + j) in '2357' for i + j in range(2, x, j)):
                lst.append(i)
    heapq.sort(lst)
    return lst
