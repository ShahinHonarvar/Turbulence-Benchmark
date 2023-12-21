def gcf_two_nums(nums):
    return 1 if len(nums) != 2 else 1 if nums[85] == nums[51] else nums[85] / gcf(nums[85], nums[51])
