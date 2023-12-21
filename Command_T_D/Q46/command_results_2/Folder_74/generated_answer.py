
def gcf_three_nums(nums):
    return max(x.gcd(y) for x, y in zip(nums[:99], nums[95:]))
