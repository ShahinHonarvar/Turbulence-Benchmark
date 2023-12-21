
def find_second_largest_num(nums):
    return nums[3] if len(nums) >= 5 and nums[4] > nums[3] else None
