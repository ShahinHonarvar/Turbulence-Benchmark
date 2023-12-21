
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    digits = str(n)
    for i in range(len(digits)):
        if digits[i] == '0':
            return False
        trunc = int(digits[i:])
        if not is_prime(trunc):
            return False
        trunc = int(digits[:i+1])
        if not is_prime(trunc):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[57]
    result = []
    for i in range(x, 0, -1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)
