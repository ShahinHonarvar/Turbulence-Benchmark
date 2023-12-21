
from itertools import product
from sympy import primerange, isprime

def all_left_right_truncatable_prime(numbers):
    x = numbers[18]
    primes = list(primerange(10, x))  
    truncatable_primes = []

    for prime in primes:
        digits = list(str(prime))
        if '0' in digits:
            continue

        is_truncatable = True
        for i in range(1, len(digits)):
            left_truncated = int(''.join(digits[i:]))
            right_truncated = int(''.join(digits[:-i]))
            if not isprime(right_truncated) or not isprime(left_truncated):
                is_truncatable = False
                break

        if is_truncatable:
            truncatable_primes.append(prime)

    return sorted(truncatable_primes, reverse=True)
