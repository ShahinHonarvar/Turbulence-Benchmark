
from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[36]
    prime_list = [
        prime for prime in range(10, x) if is_left_truncatable_prime(prime)
    ]
    return sorted(prime_list)

def is_left_truncatable_prime(n):
    if '0' in str(n) or not isprime(n):
        return False
    while n != 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:]) if len(str(n)) > 1 else 0
    return True
