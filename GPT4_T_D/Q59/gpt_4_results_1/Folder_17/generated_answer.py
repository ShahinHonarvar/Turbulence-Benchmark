
from itertools import permutations

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[36]
    primes = [str(n) for n in range(2, x) if all(is_prime(int(str(n)[:i+1])) for i in range(len(str(n))))]
    left_truncatable_primes = [int(p) for p in primes if '0' not in p and all(is_prime(int(p[i:])) for i in range(len(p)))]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes
