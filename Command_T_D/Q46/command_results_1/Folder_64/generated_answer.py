
def gcf_three_nums(nums):
    return max(gcd(x, y) for x, y, z in zip(nums, nums[8], nums[3]))
