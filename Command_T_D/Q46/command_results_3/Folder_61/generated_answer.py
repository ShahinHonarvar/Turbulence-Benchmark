
def gcf_three_nums(nums):
    return 1 if len(nums) == 0 else 1 if len(nums) == 1 else nums[0] if nums[0] == nums[1] == nums[2] else gcf_three_nums(nums[:2])
