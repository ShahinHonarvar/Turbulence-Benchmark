import itertools
def all_right_truncatable_prime(n):
    #your code here
    primes = itertools.permutations(list(range(2, n[0] + 1)), 3)
    for p in primes:
        #your code here
        if p[1] * 10**(len(p) - 2) + p[0] * 10**(len(p) - 1) <= n[0]:
            yield p
