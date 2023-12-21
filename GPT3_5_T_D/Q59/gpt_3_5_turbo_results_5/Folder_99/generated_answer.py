
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[758]
    res = []
    
    for i in range(2, x):
        if '0' in str(i):
            continue
        truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                truncatable = False
                break
        if truncatable:
            res.append(i)
    
    return sorted(res)
