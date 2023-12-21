
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[30:87])) - 1] if len(nums) > 30 else None
