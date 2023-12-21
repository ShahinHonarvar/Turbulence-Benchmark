
from math import isqrt

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_left_truncatable_prime(n):
        if len(str(n)) <= 2:
            return is_prime(n)
        return is_prime(n) and is_left_truncatable_prime(int(str(n)[1:]))
    
    def is_right_truncatable_prime(n):
        if len(str(n)) <= 2:
            return is_prime(n)
        return is_prime(n) and is_right_truncatable_prime(int(str(n)[:-1]))
    
    def is_left_right_truncatable_prime(n):
        return is_left_truncatable_prime(n) and is_right_truncatable_prime(n)
    
    x = nums[57]
    result = []
    for num in range(2, x+1):
        if is_left_right_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)
