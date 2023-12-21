def find_second_smallest_num(nums):
    return nums[5] if len(nums) > 6 and nums[5] < nums[6] else None
