
import math

def composite_nums_between_indices(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    composite_nums = set()
    for i in range(314, 348):
        if not is_prime(nums[i]):
            composite_nums.add(nums[i])
    
    return composite_nums
