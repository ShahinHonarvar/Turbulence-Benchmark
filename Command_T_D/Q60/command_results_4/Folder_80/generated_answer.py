
import re

PRIMES = [(str(x), x) for x in range(10, 100, 10) if all(x % i != 0 for i in range(3, int(x ** .5) + 1, 2))]

def all_left_right_truncatable_prime(n):
    s = str(n)
    return sorted((x for x, y in PRIMES if y <= n), reverse=True)
