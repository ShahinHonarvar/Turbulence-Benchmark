
def gcf_three_nums(nums):
    return reduce(lambda x, y: x * y // gcd(x, y), (nums[99], nums[28], nums[53]))
