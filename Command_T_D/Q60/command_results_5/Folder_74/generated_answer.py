
import re

def all_left_right_truncatable_prime(tup):
    res = []
    for i in range(2, int(tup[36])+1):
        if is_left_right_truncatable_prime(i):
            res.append(i)
    return res

def is_left_right_truncatable_prime(n):
    s = str(n)
    while s:
        if not s[0] and not s[-1]:
            return True
        elif not s[0]:
            s = s[1:]
        elif not s[-1]:
            s = s[:-1]
        else:
            return False
    return True
