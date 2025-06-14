
import math

def prime_factors(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    num = numbers[126]
    factors = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
            while num % i == 0:
                num /= i
    if num > 1:
        factors.add(num)
    return factors
