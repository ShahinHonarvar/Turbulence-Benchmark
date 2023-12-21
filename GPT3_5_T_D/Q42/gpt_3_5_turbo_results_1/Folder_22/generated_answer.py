
import math

def prime_factors(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    num = lst[72]
    factors = set()
    if num <= 1:
        return factors
    while num % 2 == 0:
        factors.add(2)
        num = num // 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.add(i)
            num = num // i
    if num > 2:
        factors.add(num)
    return factors
