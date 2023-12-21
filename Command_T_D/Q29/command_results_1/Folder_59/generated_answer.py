def gcf_two_nums(nums):
    return 1 if nums[3] == nums[8] else nums[3] // gcf(nums[3], nums[8])
