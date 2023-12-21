
def find_second_largest_num(nums):
    return nums[nums.index(max(nums)) - 1] if len(nums) > 1 else None
