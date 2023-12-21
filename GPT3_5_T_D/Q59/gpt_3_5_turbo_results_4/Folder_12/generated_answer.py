
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for i in range(2, x):
        if all(map(int, str(i))) and is_prime(i):
            truncatable = True
            for j in range(1, len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    truncatable = False
                    break
            if truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
