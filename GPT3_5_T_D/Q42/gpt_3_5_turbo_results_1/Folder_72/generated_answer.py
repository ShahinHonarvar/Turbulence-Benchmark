
import math

def prime_factors(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    factors = set()
    if len(nums) >= 17:
        num = nums[16]
        for i in range(2, int(math.sqrt(num)) + 1):
            if is_prime(i) and num % i == 0:
                factors.add(i)
    return factors
