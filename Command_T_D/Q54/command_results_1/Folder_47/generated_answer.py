import bisect
def all_right_truncatable_prime(x):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    primes += [n for n in range(49, x, 6) if all(n % d != 0 for d in range(3, int(n ** .5) + 1, 6))]
    return sorted(set(primes))
