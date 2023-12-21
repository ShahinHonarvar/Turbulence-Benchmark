import fractions
def gcf_two_nums(nums):
    x, y = map(fractions.gcd, (nums[38], nums[77])))
    return x * y // fractions.gcd(x, y)
