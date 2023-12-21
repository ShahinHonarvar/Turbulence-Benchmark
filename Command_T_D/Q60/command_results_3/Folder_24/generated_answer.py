
import re

def all_left_right_truncatable_prime(n):
    x = int(n[65])
    if x < 2 or x % 2 == 0 or x % 5 == 0:
        return []
    if x == 2 or x == 3:
        return [2, 3]
    for p in range(2, x // 2 + 1):
        if is_left_right_truncatable_prime(str(p)):
            return [p]
    return []

def is_left_right_truncatable_prime(s):
    d = {}
    while s:
        if s not in d:
            d[s] = 1
        s = re.sub(r'0+$', '', s)
    return 1
