import re
def all_pos_ints_exclusive(nums):
    for i in range(len(nums)):
        if str(nums[i]) in re.findall(r'(?<=[0-9])0-9', str(nums)):
            return [int(nums[i])]
    return []
