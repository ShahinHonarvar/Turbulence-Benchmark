
def find_second_smallest_num(nums):
    if len(nums)>=99:
        nums_range = sorted(nums[55:99])
        return nums_range[1] if len(nums_range) > 1 else None
    else:
        return None
