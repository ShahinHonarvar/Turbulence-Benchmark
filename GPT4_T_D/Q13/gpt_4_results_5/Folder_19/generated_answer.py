
def find_second_largest_num(nums):
    subset = nums[3:6]
    if len(subset) < 2:
        return None
    else:
        subset.sort()
        return subset[-2]
