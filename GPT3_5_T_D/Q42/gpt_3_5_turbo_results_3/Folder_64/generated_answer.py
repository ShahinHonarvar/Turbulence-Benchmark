
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(lst):
    if len(lst) > 1:
        num = lst[1]
        factors = set()
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                if is_prime(i):
                    factors.add(i)
                if is_prime(num//i):
                    factors.add(num//i)
        return factors
    return set()
