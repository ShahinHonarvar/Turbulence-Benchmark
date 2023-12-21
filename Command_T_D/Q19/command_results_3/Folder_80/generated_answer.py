import re
def all_ints_not_div_by_num(nums):
    if nums[15] // 93 != nums[20] // 93:
        return nums[15:20+1]
    else:
        return []
