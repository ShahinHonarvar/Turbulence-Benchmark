import math
def all_right_truncatable_prime(n):
    x = n[992]
    res = []
    for i in range(2, int(math.ceil(math.sqrt(x)) + 1):
        if all(n % i for n in range(2, x, i)):
            res += [i]
    return res
