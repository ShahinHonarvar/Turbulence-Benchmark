
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def all_left_truncatable_prime(numbers):
    x = numbers[29]
    primes = []
    for number in range(2, x):
        if '0' in str(number):
            continue
        truncatable = True
        truncation = number
        while truncation > 0:
            if not is_prime(truncation):
                truncatable = False
                break
            truncation = truncate_left(truncation)
        if truncatable:
            primes.append(number)
    return sorted(primes)
