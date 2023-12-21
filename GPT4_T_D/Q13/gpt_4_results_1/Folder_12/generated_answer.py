
def find_second_largest_num(nums):
    if len(nums) < 65:
        return None
    else:
        subset = nums[14:65]
        subset.sort()
        return subset[-2] if len(subset) > 1 else None
