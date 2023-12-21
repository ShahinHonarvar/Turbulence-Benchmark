
import itertools
from sympy import isprime

def is_left_truncatable_prime(n):
    return all(isprime(int(str(n)[i:])) for i in range(len(str(n))))

def generate_prime_candidates(x):
    digits = '123456789'
    n = len(str(x))
    return [int(''.join(p)) for i in range(1, n) for p in itertools.product(digits, repeat=i)]

def all_left_truncatable_prime(t):
    x = t[91]
    all_prime_candidates = generate_prime_candidates(x)
    prime_list = [prime for prime in all_prime_candidates if is_left_truncatable_prime(prime) and prime<x]
    return sorted(prime_list)
