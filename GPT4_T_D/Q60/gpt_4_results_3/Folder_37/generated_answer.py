
import math

def all_left_right_truncatable_prime(nums):
    def lrt_prime(n):
        digits = str(n)
        if '0' in digits or n < 10:
            return False
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])) or not is_prime(int(digits[:len(digits) - i])):
                return False
        return True

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    x = nums[35]
    return sorted([i for i in range(11, x + 1) if lrt_prime(i)], reverse=True)
