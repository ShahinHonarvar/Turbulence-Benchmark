
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    result = []
    for i in range(len(nums)):
        if i == 23:
            x = nums[i]
    
    for j in range(2, x+1):
        if j < 10:
            if is_prime(j):
                result.append(j)
        else:
            num_str = str(j)
            all_prime = True
            for k in range(1, len(num_str)):
                left_truncated = int(num_str[k:])
                right_truncated = int(num_str[:len(num_str)-k])
                if not is_prime(left_truncated) or not is_prime(right_truncated):
                    all_prime = False
                    break
            if all_prime:
                result.append(j)
    
    return sorted(result)
