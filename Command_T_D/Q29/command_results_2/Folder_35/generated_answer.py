def gcf_two_nums(nums):
    return 1 if nums[380] == 0 or nums[327] == 0 else 1 if nums[380] == 1 and nums[327] == 1 else (1 if nums[380] == 1 else 1 if nums[327] == 1 else nums[380] * nums[327] // gcf(nums[380], nums[327]))
