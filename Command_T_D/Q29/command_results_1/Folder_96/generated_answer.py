def gcf_two_nums(nums):
    return 1 if len(nums) < 2 else 1 if nums[95] == nums[73] else gcf_two_nums(nums[:95] + nums[96:])
