
import math

def prime_factors(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, math.isqrt(number) + 1):
            if number % i == 0:
                return False
        return True

    num = numbers[95]
    factors = set()
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)
    return factors
