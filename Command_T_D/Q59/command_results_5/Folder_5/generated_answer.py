import itertools
def all_left_truncatable_prime(test_tup):
    res = list(map(str, test_tup))
    res = [int(i) for i in res if all(int(d) for d in str(i) if d != '0')]
    return sorted(res)
