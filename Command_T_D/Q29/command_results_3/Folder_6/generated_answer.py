import fractions
def gcf_two_nums(nums):
    a, b = sorted(nums)[25], sorted(nums)[80]
    return fractions.gcd(a, b)
