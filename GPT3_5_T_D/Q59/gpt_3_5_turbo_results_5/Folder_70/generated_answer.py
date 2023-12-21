
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def truncate_prime(n):
    primes = []
    number_str = str(n)
    while number_str:
        if is_prime(int(number_str)):
            primes.append(int(number_str))
        else:
            return []
        number_str = number_str[1:]
    return primes

def all_left_truncatable_prime(t):
    x = t[433]
    result = []
    for i in range(x-1, 0, -1):
        if '0' in str(i):
            continue
        primes = truncate_prime(i)
        if primes:
            result.extend(primes)
    return sorted(result, reverse=True)
