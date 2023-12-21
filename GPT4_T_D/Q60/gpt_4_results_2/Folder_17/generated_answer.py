
import math

def all_left_right_truncatable_prime(nums):
    x = nums[36]
    
    def is_prime(n):
        if n in (0, 1):
            return False
        for i in range(2, math.isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        len_str_n = len(str_n)
        for i in range(len_str_n):
            if not (is_prime(int(str_n[i:])) and is_prime(int(str_n[:len_str_n-i]))):
                return False
        return True

    result = []
    for i in range(x, 11, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return result
