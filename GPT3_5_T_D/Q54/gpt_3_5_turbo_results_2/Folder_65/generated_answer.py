
import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[32]
    result = []
    for i in range(2, x):
        if is_prime(i):
            remove_last = int(str(i)[:-1])
            while remove_last >= 10:
                if not is_prime(remove_last):
                    break
                remove_last = int(str(remove_last)[:-1])
            else:
                result.append(i)
    return sorted(result)
