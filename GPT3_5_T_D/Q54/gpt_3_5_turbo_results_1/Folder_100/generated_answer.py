
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[26]
    result = []
    for num in range(2, x):
        truncated = str(num)
        while len(truncated) > 0:
            if not is_prime(int(truncated)):
                break
            truncated = truncated[:-1]
        else:
            result.append(num)
    return sorted(result)
