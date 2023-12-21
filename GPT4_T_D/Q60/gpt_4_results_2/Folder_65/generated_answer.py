
from itertools import product

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def get_permutations(n):
    digits = '123456789'
    return [''.join(p) for i in range(1, n+1) for p in product(digits, repeat=i)]

def is_left_right_truncatable(prime):
    for i in range(1, len(prime)):
        if not is_prime(int(prime[i:])) or not is_prime(int(prime[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[32]
    primes = sorted(set(int(p) for p in get_permutations(len(str(x))) if is_prime(int(p))))
    return [p for p in primes if p <= x and is_left_right_truncatable(str(p))]
