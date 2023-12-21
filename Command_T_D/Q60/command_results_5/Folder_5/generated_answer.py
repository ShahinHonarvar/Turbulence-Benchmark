
import math
import itertools

def all_left_right_truncatable_prime(x):
    return sorted(set(itertools.filter(left_right_truncatable_prime, range(2, x+1))), key=lambda p: str(p))

def left_right_truncatable_prime(n):
    d = str(n)
    if d[0] == '0':
        return False
    if d[-1] == '0':
        return False
    if d[0] == '1' and d[-1] == '1':
        return True
    for i in range(1, len(d)-1):
        if d[i] == '0':
            return False
        if d[i] == '1':
            break
    if d[0] == '1':
        return True
    if d[-1] == '1':
        return True
    return True
