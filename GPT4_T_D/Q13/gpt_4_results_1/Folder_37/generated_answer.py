
def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    else:
        subset = sorted(nums[1:6], reverse=True)
        return subset[1] if len(subset) > 1 else None
