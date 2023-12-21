def gcf_two_nums(nums):
    return 1 if len(nums) == 0 else gcf_two_nums(nums[1:]) if len(nums) == 1 else nums[0] * nums[1] // gcf_two_nums(nums[2:])
