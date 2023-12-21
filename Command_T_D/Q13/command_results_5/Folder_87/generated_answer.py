
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:36]) + 1) if 36 <= len(nums) - 1 else None]
