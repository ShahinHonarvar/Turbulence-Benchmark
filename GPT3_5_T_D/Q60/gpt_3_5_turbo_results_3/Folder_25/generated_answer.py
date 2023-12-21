
import math

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[92]
    primes = set()
    
    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        while len(num_str) > 1:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[1:-1]
        return True
    
    for num in range(2, x + 1):
        if is_left_right_truncatable_prime(num):
            primes.add(num)
    
    return sorted(list(primes))
