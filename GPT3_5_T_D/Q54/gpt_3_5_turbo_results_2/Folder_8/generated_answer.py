
from math import isqrt
from itertools import product

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[41]
    primes = []
    truncatable_primes = []
    for i in range(2, x):
        if is_prime(i):
            primes.append(i)
    for prime in primes:
        if prime < 10:
            truncatable_primes.append(prime)
        else:
            digits = str(prime)
            flag = True
            for j in range(1, len(digits)):
                number = int(digits[:j])
                if number not in primes:
                    flag = False
                    break
            if flag:
                truncatable_primes.append(prime)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes
