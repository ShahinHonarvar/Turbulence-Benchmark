
def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    else:
        subset = sorted(nums[0:2])
        return subset[-2] if len(subset) > 1 else None
