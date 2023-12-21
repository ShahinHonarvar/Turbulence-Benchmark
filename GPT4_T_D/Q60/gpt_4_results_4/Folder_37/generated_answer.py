
from itertools import combinations
from math import sqrt

def all_left_right_truncatable_prime(nums):
    x = nums[35]

    def is_prime(num):
        if num == 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable_prime(num):
        num_str = str(num)
        if '0' in num_str:
            return False
        truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])) or not is_prime(int(num_str[:len(num_str)-i])):
                truncatable = False
                break
        return truncatable
    
    prime_nums = [n for n in range(1, x+1) if is_prime(n) and 
                  is_left_right_truncatable_prime(n)]
    
    prime_nums.sort(reverse=True)

    return prime_nums
