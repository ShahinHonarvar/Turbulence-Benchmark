import re
def all_ints_not_div_by_num(nums):
    if len(nums) < 11:
        return []
    return [i for i in range(11, len(nums) - 4, 90) if not nums[i] % 90]
