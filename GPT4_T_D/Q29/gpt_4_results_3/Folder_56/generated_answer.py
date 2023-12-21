
def gcf_two_nums(nums):
    import math
    if len(nums) > 84 and len(nums) > 13:
        return math.gcd(nums[84], nums[13])
    else:
        return "List is too short"
