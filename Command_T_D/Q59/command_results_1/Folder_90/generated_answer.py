import math
def all_left_truncatable_prime(test_tup):
    res = []
    for x in range(2, int(test_tup[0]) + 1):
        is_prime = True
        for i in range(1, int(math.log10(x)) + 1):
            if x % 10**i == 0:
                is_prime = False
                break
        if is_prime:
            res.append(x)
    return res
