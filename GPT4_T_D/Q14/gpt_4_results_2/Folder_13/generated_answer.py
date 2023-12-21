
def find_second_smallest_num(nums):
    if len(nums) < 33:
        return None
    else:
        subset = nums[28:33]
        subset.sort()
        if len(subset) < 2:
            return None
        else:
            return subset[1]
