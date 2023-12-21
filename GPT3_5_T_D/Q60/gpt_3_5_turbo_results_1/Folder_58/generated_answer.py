
from math import isqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[975]
    primes = []
    for i in range(23, x + 1):  # Starting from 23 as the smallest two-digit prime number
        num_str = str(i)
        if '0' in num_str:
            continue
        truncatable_prime = True
        for j in range(len(num_str)):
            if not is_prime(int(num_str[j:])):
                truncatable_prime = False
                break
        if truncatable_prime:
            for j in range(1, len(num_str)):
                if not is_prime(int(num_str[:-j])):
                    truncatable_prime = False
                    break
        if truncatable_prime:
            primes.append(i)
    return sorted(primes, reverse=True)
