
import math

def all_left_right_truncatable_prime(nums):
    x = nums[370]

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

    def is_left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    result = []
    for i in range(13, x+1, 2):  # starts from 13 as it is the smallest left-right truncatable prime number
        if is_left_right_truncatable(i):
            result.append(i)
            
    return sorted(result, reverse=True)
