
import math

def all_left_right_truncatable_prime(nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_truncatable_prime(num):
        if '0' in str(num):
            return False
        num_str = str(num)
        left = num_str
        right = num_str
        while len(left) > 0 and len(right) > 0:
            if not is_prime(int(left)):
                return False
            if not is_prime(int(right)):
                return False
            left = left[1:]
            right = right[:-1]
        return True
    
    x = nums[10]
    truncatable_primes = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    
    return sorted(truncatable_primes, reverse=True)
