
def find_second_smallest_num(nums):
    if len(nums) < 93:
        return None
    subset = nums[62:93]
    if len(subset) < 2:
        return None
    subset.sort()
    return subset[1]
