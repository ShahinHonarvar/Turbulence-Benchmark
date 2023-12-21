
from sympy import isprime

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    all_primes = list(filter(isprime, range(1, x)))
    truncatable_primes = []
    for prime in all_primes:
        if '0' in str(prime):
            continue
        num_len = len(str(prime))
        for i in range(num_len):
            if not isprime(int(str(prime)[i:])):
                break
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes, reverse=True)
