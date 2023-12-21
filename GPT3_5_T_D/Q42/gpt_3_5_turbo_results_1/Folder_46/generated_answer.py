
import math

def prime_factors(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    index = 453
    number = numbers[index]
    factors = set()
    for i in range(2, math.isqrt(number) + 1):
        if number % i == 0 and is_prime(i):
            factors.add(i)
    return factors
