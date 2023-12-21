
def find_second_smallest_num(nums):
    nums = sorted(nums)
    return nums[4] if len(nums) > 5 else None
