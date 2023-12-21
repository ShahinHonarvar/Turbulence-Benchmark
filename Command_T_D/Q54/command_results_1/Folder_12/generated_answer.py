import sys
def all_right_truncatable_prime(n):
    s = str(n)
    l = len(s)
    res = []
    for i in range(l):
        p = int(s[:i])
        q = int(s[i:])
        if q < n:
            res += [p]
            break
    return res
