
def find_second_largest_num(nums):
    return nums[nums.index(max(nums[:65]), start=66) - 1][-1] if len(nums) > 65 else None
