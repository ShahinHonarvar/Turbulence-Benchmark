
from sympy import sieve

def all_left_truncatable_prime(numbers):
    x = numbers[50]
    primes = set(sieve.primerange(0, x))
    def is_left_truncatable_prime(n):
        while n > 0:
            if n not in primes:
                return False
            n //= 10
        return True

    result = []
    for n in range(x, 0, -1):
        if n not in primes or '0' in str(n):
            continue
        if is_left_truncatable_prime(n):
            result.append(n)
    return result
