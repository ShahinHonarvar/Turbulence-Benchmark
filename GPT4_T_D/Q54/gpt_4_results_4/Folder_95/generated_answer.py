
import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_right_truncatable_prime(tup):
    x = tup[77]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    return sorted(primes)
