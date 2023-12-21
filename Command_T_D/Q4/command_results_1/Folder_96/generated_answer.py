import re
def all_pos_ints_exclusive(nums):
    for i in range(50, 200):
        if str(i) in nums:
            return [int(nums[str(i)])]
    return []
