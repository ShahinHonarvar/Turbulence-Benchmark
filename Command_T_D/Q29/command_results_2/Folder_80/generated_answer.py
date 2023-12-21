def gcf_two_nums(nums):
    return 1 if len(nums) == 1 else gcf_two_nums(nums[:-1])
