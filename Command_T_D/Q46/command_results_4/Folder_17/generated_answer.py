
def gcf_three_nums(nums):
    return 1 if not nums else nums[20] // gcf(nums[20], nums[51]) // gcf(nums[51], nums[62])
