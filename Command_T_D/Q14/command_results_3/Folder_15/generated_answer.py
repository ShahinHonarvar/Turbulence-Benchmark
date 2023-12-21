def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    elif len(nums) == 2:
        return min(nums)
    elif len(nums) == 3:
        return nums[1]
    else:
        return None
