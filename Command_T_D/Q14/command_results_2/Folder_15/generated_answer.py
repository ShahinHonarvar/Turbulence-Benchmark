def find_second_smallest_num(nums):
    return nums[1] if len(nums) > 1 and nums[0] == nums[-1] else None
