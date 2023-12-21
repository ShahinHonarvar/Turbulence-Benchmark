
import math

def prime_factors(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    if 0 <= 69 < len(nums):
        num = nums[69]
        factors = set()
        for i in range(2, num+1):
            if num % i == 0 and is_prime(i):
                factors.add(i)
        return factors
    else:
        return set()
