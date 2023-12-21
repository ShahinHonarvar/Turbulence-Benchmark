
def gcf_three_nums(nums):
    return 1 if nums[19] == 1 and nums[94] == 1 and nums[78] == 1 else nums[19] * nums[94] * nums[78] // gcf(nums[19], nums[94], nums[78])
