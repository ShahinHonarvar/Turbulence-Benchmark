
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[97]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncated = str(i)
            while len(truncated) > 0:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[:-1]
            else:
                primes.append(i)
    return sorted(primes, reverse=True)
