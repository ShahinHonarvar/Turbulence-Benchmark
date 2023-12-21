import math
def all_right_truncatable_prime(x):
    res = []
    for p in range(3, int(math.ceil(math.sqrt(x)) + 1, 2):
        if p == x:
            break
        if p % 2 == 0:
            continue
        if p % 5 == 0:
            continue
        if str(p) in str(x):
            break
        res.append(p)
    return res
