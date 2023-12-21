
def find_second_largest_num(nums):
    if len(nums) < 30:
        return None
    subset = nums[29:52]
    if len(subset) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]
