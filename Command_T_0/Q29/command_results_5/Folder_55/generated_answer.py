def gcf_two_nums(nums):
    return 1 if len(nums) == 0 else nums[0] if nums[0] == nums[1] else gcf_two_nums(nums[:-1])
