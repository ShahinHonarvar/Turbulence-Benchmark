import re
import bisect
def all_left_truncatable_prime(n):
    if n[0]=='0':
        return []
    x = int(re.sub(r'0*', '', str(n[0])))
    d = [x]
    for i in range(2, int(x**0.5) + 1):
        d += [x-i]
    return sorted(set(d))
