
import sys
import bisect

sys.setrecursionlimit(1_000_000)

def return_binary_or_hexa(s):
    a, b = s[36], s[85]
    L = []
    for i in range(a + 1, b - 1):
        if i not in s:
            L.append(i)
    s += L
    if len(s) % 2 == 1:
        return format(sum(s), 'b')
    else:
        return format(sum(s), 'x')
