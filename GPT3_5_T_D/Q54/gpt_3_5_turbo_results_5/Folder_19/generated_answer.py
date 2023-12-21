
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[67]
    result = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            truncatable = True
            current_num = n
            while current_num > 9:
                current_num = current_num // 10
                if not is_prime(current_num):
                    truncatable = False
                    break
            if truncatable:
                result.append(n)
    return sorted(result, reverse=True)
