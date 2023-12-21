
from itertools import product
from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[96]
    leftright_primes = []
    for n_digits in range(1, len(str(x))+1):
        for digits in product('123456789', repeat=n_digits):
            candidate = int(''.join(digits))
            if candidate > x:
                continue
            if all(isprime(int(''.join(digits[:i]))) and isprime(int(''.join(digits[i:]))) for i in range(1, n_digits)):
                leftright_primes.append(candidate)
    return sorted(leftright_primes, reverse=True)
