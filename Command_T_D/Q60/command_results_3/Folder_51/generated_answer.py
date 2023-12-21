
import sys
input = sys.stdin.readline

def all_left_right_truncatable_prime(x):
    res = []
    for y in range(x-2, 1, -1):
        if y > 9:
            continue
        if y > 2:
            if is_left_right_truncatable_prime(y):
                res.append(y)
        else:
            res.append(y)
    return res

def is_left_right_truncatable_prime(x):
    return x > 1 and all(int(d) for d in str(x))
