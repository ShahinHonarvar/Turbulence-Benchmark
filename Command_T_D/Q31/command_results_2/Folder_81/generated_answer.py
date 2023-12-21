import sys
import heapq
def if_perfect_num(a):
    if len(a) < 20:
        return False
    s = []
    for i in range(20, len(a)):
        s.append(a[i])
        s.append(s[-1] + a[i])
    s = heapq.nlargest(len(s), s)
    return s[0] == s[1] == s[2] == a[20]
