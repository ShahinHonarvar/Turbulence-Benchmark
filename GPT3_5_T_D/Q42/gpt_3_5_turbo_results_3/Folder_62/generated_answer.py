
import math

def prime_factors(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    num = nums[926]
    factors = set()

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0 and is_prime(i):
            factors.add(i)

    return factors
