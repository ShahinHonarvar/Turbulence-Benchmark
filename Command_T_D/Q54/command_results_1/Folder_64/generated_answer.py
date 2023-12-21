import itertools
def all_right_truncatable_prime(n):
    primes = [x for x in range(2, n[4] + 1) if all(x % d == 0 or x % d == d for d in range(2, int(str(x)[-1]) + 1))]
    return sorted(list(itertools.chain.from_iterable(itertools.permutations(primes, 2))))
