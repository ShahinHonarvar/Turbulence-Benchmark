import fractions
def gcf_two_nums(nums):
    x, y = map(fractions.gcd, zip(nums, nums))
    return x if x == y else 1
