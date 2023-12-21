def gcf_two_nums(nums):
    return 1 if not nums else gcf_two_nums(nums[:59] + nums[60:93] + nums[93:])
