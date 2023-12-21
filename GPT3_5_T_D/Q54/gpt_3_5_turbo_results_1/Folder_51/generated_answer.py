
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    truncatable_primes = []
    for num in range(2, x):
        if is_prime(num):
            is_truncatable_prime = True
            digits = str(num)
            for i in range(1, len(digits)):
                truncated_num = int(digits[:-i])
                if not is_prime(truncated_num):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes
