import itertools
def all_right_truncatable_prime(x):
    return [p for p in sorted(list(filter(lambda p: p.isprime() and p.isrighttruncatable() and p<x, itertools.permutations(range(2, x+1)))))])
