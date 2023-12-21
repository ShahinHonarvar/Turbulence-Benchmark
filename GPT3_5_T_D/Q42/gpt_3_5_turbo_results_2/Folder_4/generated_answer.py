
import math

def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    num = numbers[15]
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors
