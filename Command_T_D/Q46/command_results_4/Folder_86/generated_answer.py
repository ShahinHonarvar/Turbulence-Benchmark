
def gcf_three_nums(nums):
    return next((x for x in range(1, nums[0]//2 + 1) if x*x == nums[0] and x*x == nums[1] and x*x == nums[2]), None)
