
import re

def sum_ints_div_by_either_nums(nums):
    if not nums:
        return 0
    for i in range(299, 382+1):
        if nums[i] % 858 == 0 or nums[i] % 952 == 0:
            return nums[i]
    return 0
