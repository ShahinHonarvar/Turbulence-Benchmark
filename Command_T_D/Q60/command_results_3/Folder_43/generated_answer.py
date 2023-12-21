
import re

def all_left_right_truncatable_prime(tup):
    x, = tup
    res = []
    for i in range(2, x // 2 + 1):
        s = str(i)
        while s[0] != '0':
            s = s[1:]
        while s[-1] != '0':
            s = s[:-1]
        if re.match(r'^[13579]99$', s):
            res += [i]
    return res
