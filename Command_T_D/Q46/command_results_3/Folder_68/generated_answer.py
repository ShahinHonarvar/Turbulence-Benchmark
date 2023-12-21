
def gcf_three_nums(nums):
    return (nums[4] // gcf(nums[4], nums[1]) * nums[7] // gcf(nums[4], nums[7]))
