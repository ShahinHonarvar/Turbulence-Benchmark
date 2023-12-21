
from sympy import isprime

def left_truncatable_prime(n):
    n_str = str(n)[::-1]
    return all(isprime(int(n_str[i:][::-1])) for i in range(len(n_str)))

def all_left_truncatable_prime(t):
    x = t[945]
    return sorted([y for y in range(2, x) if left_truncatable_prime(y)], reverse=True)
