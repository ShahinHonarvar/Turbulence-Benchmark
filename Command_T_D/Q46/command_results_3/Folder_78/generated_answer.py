
def gcf_three_nums(nums):
    return (nums[13] // gcf(nums[13], nums[70], nums[32]) * nums[70] // gcf(nums[13], nums[70], nums[32]) * nums[32] // gcf(nums[13], nums[70], nums[32]))
