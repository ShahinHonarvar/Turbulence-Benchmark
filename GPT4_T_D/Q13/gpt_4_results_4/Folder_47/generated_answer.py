
def find_second_largest_num(nums):
    subset = nums[37:77]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]
