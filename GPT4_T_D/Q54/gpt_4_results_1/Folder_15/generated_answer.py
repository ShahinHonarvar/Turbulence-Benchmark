
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqr = int(math.sqrt(n)) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    str_n = str(n)
    for _ in range(len(str_n)):
        if not is_prime(int(str_n)):
            return False
        str_n = str_n[:-1]
    return True

def all_right_truncatable_prime(tup):
    x = tup[6]
    right_truncatable_primes = []
    for n in range(2, x):
        if is_right_truncatable_prime(n):
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)
