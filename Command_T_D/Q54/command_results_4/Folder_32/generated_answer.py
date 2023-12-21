import math
def all_right_truncatable_prime(test_tup):
    res = []
    x = test_tup[42]
    for i in range(2, x//2 + 1):
        if all(n % d for d in range(2, int(math.log(n, 2)) + 1)):
            res.append(i)
    return res
