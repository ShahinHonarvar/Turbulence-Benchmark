
from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    n_str = str(n)
    for i in range(len(n_str)):
        left_trunc = int(n_str[i:])
        right_trunc = int(n_str[:len(n_str)-i])
        if not is_prime(left_trunc) or not is_prime(right_trunc):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    truncatable_primes = []
    for i in range(2, x+1):
        if is_truncatable_prime(i):
            truncatable_primes.append(i)
    return sorted(truncatable_primes)
