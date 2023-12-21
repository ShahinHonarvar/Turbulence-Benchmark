
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[86]
    truncatable_primes = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            digit = i % 10
            while digit in {1, 3, 7, 9} and i > digit:
                i //= 10
                if not is_prime(i):
                    break
                digit = i % 10
            else:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
