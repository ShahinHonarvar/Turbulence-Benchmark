
def gcf_three_nums(lst):
    import math
    nums = [lst[96], lst[57], lst[85]]
    gcf = math.gcd(nums[0], nums[1])
    gcf = math.gcd(gcf, nums[2])
    return gcf
