import fractions
def gcf_two_nums(nums):
    x, y = map(fractions.gcd, (nums[47], nums[10]))
    return 1 if x == 1 else x
