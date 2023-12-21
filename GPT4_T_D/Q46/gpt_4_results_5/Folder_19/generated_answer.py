
def gcf_three_nums(nums):
    from math import gcd
    try:
        gcf = gcd(gcd(nums[40], nums[15]), nums[99])
        return gcf
