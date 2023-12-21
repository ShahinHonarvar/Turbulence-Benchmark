
import math

def is_prime(n):
    if n == 0 or n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

def is_right_truncatable_prime(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = n//10
    return True

def all_right_truncatable_prime(nums):
    x = nums[54]
    return sorted([i for i in range(x) if is_right_truncatable_prime(i)], reverse=True)
