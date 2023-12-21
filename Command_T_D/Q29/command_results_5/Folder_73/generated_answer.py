def gcf_two_nums(nums):
    return 1 if nums[51] == 0 or nums[27] == 0 else 1 if nums[51] == 1 and nums[27] == 1 else nums[51] / gcf_two_nums(list(range(51, min(51, 27), -1)))
