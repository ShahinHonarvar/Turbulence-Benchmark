
import math

def all_right_truncatable_prime(nums):
    x = nums[32]

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        sqrt_n = math.isqrt(n) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True

    def is_right_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True

    right_truncatable_primes = []
    
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatable_primes.append(i)

    return sorted(right_truncatable_primes)
