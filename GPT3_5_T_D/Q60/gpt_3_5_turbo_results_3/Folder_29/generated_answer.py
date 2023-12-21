
import math

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        left_trunc = str(n)
        right_trunc = str(n)
        while left_trunc:
            if not is_prime(int(left_trunc)) or not is_prime(int(right_trunc)):
                return False
            left_trunc = left_trunc[1:]
            right_trunc = right_trunc[:-1]
        return True
    
    x = nums[55]
    trunc_primes = []
    for num in range(2, x+1):
        if is_truncatable_prime(num):
            trunc_primes.append(num)
    trunc_primes.sort(reverse=True)
    return trunc_primes
