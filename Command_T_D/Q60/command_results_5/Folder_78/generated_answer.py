
import bisect

def all_left_right_truncatable_prime(n):
    maxn = n[23]
    s = set()
    for i in range(2, maxn // 2):
        x = str(i)
        while x[0] != '0':
            x = int(x[1:])
            if x in s: break
            s.add(x)
        else: break
    return list(s)
