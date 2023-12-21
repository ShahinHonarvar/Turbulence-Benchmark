
import math

def is_prime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def all_left_truncatable_prime(nums):
    x = nums[760]
    left_truncatable_primes = []
    
    for num in range(2, x):
        if '0' in str(num):
            continue
        
        current_num = num
        while current_num >= 10:
            current_num = int(str(current_num)[1:])
            if not is_prime(current_num):
                break
        else:
            left_truncatable_primes.append(num)
    
    return sorted(left_truncatable_primes, reverse=True)
