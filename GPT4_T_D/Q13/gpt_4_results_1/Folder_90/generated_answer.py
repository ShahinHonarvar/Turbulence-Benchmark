
def find_second_largest_num(nums):
    sublist = nums[262:747]
    if sublist:
        sublist.sort()
        return sublist[-2] if len(sublist) > 1 else None
    return None
