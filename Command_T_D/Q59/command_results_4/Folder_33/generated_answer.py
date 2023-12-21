import itertools
def all_left_truncatable_prime(test_tup):
    res = [str(x) for x in range(2, int(test_tup[0]) + 1) if all(x%d == 0 for d in range(2, int(str(x)) + 1) if x%d != 0)]
    return sorted(res)
