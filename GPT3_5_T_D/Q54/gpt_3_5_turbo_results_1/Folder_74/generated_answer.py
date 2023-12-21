
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[36]
    result = []
    for num in range(2, x):
        if is_prime(num):
            num_str = str(num)
            is_truncatable = True
            for i in range(1, len(num_str)):
                trunc_num = int(num_str[:i])
                if not is_prime(trunc_num):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(num)
    return sorted(result)
