
from math import isqrt

def all_left_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(number):
        if '0' in str(number):
            return False

        for i in range(1, len(str(number))):
            left_truncated = int(str(number)[i:])
            right_truncated = int(str(number)[:-i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False

        return True

    x = nums[618]
    result = []

    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)

    return result
