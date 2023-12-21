
def gcf_three_nums(nums):
    return max(gcd(x, y) for x, y in zip(nums[252:], nums[:149]))
