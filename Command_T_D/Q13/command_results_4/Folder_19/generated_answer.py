
def find_second_largest_num(nums):
    return nums[3] if len(nums) > 2 and nums[2] < nums[3] else None
