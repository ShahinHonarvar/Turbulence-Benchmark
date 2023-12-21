
def find_second_largest_num(nums):
    nums = nums[26:53]
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None
