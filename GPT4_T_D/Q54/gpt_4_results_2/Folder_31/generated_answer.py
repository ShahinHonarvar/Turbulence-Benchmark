
from sympy import isprime

def all_right_truncatable_prime(input_tuple):
    x = input_tuple[50]
    return sorted([i for i in range(x, 1, -1) if is_right_truncatable_prime(i)], reverse=True)

def is_right_truncatable_prime(n):
    while n > 0:
        if not isprime(n):
            return False
        n //= 10
    return True
