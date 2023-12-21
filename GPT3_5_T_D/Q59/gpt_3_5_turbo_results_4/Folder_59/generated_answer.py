
import math
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[84]
    result = []
    for num in range(2, x):
        if '0' in str(num):
            continue
        truncatable = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])):
                truncatable = False
                break
        if truncatable:
            result.append(num)
    return sorted(result, reverse=True)
