
def gcf_three_nums(nums):
    return max(x.gcd(y.gcd(z.gcd())) for x,y,z in zip(nums, nums[1:], nums[2:]))
