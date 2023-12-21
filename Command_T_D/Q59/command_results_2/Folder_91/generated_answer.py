import itertools
def all_left_truncatable_prime(tup):
    x = tup[0]
    return sorted(itertools.takewhile(lambda n: n and all(str(n)[i] in '2357' for i in range(1, len(str(n)))), x-1))
