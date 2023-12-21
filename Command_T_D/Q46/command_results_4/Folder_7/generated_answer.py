
def gcf_three_nums(nums):
    return (nums[477] // gcf(nums[477], nums[696]) // gcf(nums[477], nums[663]) - 1)
