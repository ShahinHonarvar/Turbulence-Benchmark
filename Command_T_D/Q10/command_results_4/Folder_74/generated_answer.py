import re
def all_odd_ints_exclusive(nums):
    if nums[12] % 2 != 0:
        idx = 13
    else:
        idx = 14
    return [x for x in nums[idx:70]]
