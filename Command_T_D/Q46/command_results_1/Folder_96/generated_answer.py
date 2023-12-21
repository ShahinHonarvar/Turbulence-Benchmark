
def gcf_three_nums(nums):
    return reduce(lambda x, y: x * y // gcd(x, y), (nums[29], nums[74], nums[49]), 1)
