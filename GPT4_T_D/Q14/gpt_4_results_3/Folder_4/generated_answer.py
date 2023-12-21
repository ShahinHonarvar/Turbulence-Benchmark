
def find_second_smallest_num(nums):
    if len(nums) < 85:
        return None
    else:
        subset = nums[70:85]
        subset.sort()
        if len(subset) > 1:
            return subset[1]
        else:
            return None
