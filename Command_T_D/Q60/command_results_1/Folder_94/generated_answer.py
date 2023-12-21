
import re

def all_left_right_truncatable_prime(n):
    res = []
    for x in range(2, n[0] + 1):
        for y in range(x, n[0] + 1):
            if x > y:
                break
            if is_left_right_truncatable_prime(x):
                res.append(x)
            if is_left_right_truncatable_prime(y):
                res.append(y)
    return res

def is_left_right_truncatable_prime(x):
    return x > 1 and all(int(d) > 0 for d in str(x))
