import sys
def gcf_two_nums(nums):
    return 1 if len(nums) < 2 else gcf_two_nums(nums[:-1]) if nums[0] == nums[-1] else gcf_two_nums(nums[:-1]) if nums[0] != nums[-1] else 1
