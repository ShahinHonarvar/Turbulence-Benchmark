
def gcf_three_nums(nums):
    return max(x.gcd(y.gcd(z.gcd(x, y, z))) for x, y, z in zip(nums[:40], nums[15:], nums[99:]))
