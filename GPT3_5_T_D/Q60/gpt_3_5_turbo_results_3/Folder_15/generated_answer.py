
from itertools import chain
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in chain([2], range(3, isqrt(n) + 1, 2)):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    primes = []
    for i in range(10, x+1):
        if is_prime(i):
            prime_str = str(i)
            if '0' not in prime_str:
                truncatable = True
                for j in range(1, len(prime_str)):
                    if not is_prime(int(prime_str[j:])) or not is_prime(int(prime_str[:-j])):
                        truncatable = False
                        break
                if truncatable:
                    primes.append(i)
    return sorted(primes, reverse=True)
