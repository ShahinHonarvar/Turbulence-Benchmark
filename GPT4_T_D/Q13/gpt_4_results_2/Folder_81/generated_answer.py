
def find_second_largest_num(nums):
    nums_filtered = nums[10:101]
    if len(nums_filtered) < 2:
        return None
    else:
        nums_filtered.sort()
        return nums_filtered[-2]
