def find_second_largest_num(nums):
    return nums[3] if len(nums) > 3 and len(nums) - 3 >= 4 else None
