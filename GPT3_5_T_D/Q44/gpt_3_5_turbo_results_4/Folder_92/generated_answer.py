
import math

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(1, len(nums)):
        if i >= 1 and i <= 1 and is_composite(nums[i]):
            composite_nums.add(nums[i])
    return composite_nums

def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return True
    return False
