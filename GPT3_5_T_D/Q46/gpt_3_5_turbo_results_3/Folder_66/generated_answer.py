
def gcf_three_nums(lst):
    import math
    nums = [lst[92], lst[69], lst[95]]
    gcf = math.gcd(nums[0], math.gcd(nums[1], nums[2]))
    return gcf
