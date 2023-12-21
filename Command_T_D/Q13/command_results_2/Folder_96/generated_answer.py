
def find_second_largest_num(nums):
    idx = nums.index(max(nums[:15])) + 15
    return nums[idx] if idx < len(nums) - 1 else None
