
def gcf_three_nums(lst):
    nums = sorted(set(lst), key=lambda x: x)[:3]
    return gcd(nums[0], gcd(nums[1], nums[2]))
