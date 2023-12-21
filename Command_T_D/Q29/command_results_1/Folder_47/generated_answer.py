import fractions
def gcf_two_nums(nums):
    a, b = map(fractions.gcd, (nums[28], nums[17]))
    return a * b // fractions.gcd(a, b)
