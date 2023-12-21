
def find_second_largest_num(nums):
    nums = sorted(set(nums))
    return nums[len(nums) - 2] if len(nums) > 1 else None
