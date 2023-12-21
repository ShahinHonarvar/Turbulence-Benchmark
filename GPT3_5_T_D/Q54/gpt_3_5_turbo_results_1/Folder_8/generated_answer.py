
import math

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[41]
    results = []
    for num in range(2, x):
        if is_prime(num):
            truncatable = True
            temp = num
            while temp > 0:
                temp //= 10
                if not is_prime(temp):
                    truncatable = False
                    break
            if truncatable:
                results.append(num)
    return sorted(results, reverse=True)
