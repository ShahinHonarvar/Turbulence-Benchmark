
def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    return nums[2] if len(nums) == 3 else nums[3] if nums[2] == nums[3] else nums[3]
