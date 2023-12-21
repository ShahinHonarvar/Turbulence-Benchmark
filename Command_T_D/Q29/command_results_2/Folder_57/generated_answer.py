import fractions
def gcf_two_nums(nums):
    a, b = map(fractions.gcd, (nums[28], nums[49]))
    return max(a, b)
