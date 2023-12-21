import itertools
def all_left_truncatable_prime(n):
    res = list(itertools.takewhile(lambda x: x.is_prime(), (x for x in range(2, n[23] + 1) if x.is_prime() and x.lstrip(str(x)) == str(x))))
    return sorted(res)
