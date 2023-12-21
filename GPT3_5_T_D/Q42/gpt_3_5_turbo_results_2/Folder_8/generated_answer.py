
import math

def prime_factors(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_factors_set = set()
    num = nums[49]
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            prime_factors_set.add(i)

    return prime_factors_set
