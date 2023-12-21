
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[67]
    primes = []
    for i in range(1, len(str(x))):
        for j in range(1, 10):
            n = int(str(j) + str(x)[i:])
            if is_prime(n) and '0' not in str(n):
                primes.append(n)
    return sorted(primes, reverse=True)
