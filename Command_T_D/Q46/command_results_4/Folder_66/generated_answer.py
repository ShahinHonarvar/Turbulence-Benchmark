
def gcf_three_nums(nums):
    return 1 if len(nums) == 0 else nums[0] if len(nums) == 1 else gcf_three_nums(nums[:-1]) if len(nums) == 2 else nums[0] * nums[1] // gcf_three_nums(nums[:-1])
