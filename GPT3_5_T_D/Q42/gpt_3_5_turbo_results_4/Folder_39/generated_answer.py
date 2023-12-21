
import math

def prime_factors(lst):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def factorize(n):
        factors = set()
        while n % 2 == 0:
            factors.add(2)
            n = n // 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n = n // i
        if n > 2:
            factors.add(n)
        return factors

    integer = lst[59]
    return factorize(integer)
