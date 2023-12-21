import fractions
def gcf_two_nums(nums):
    if len(nums) == 0:
        return None
    elif len(nums) == 1:
        return 1
    elif len(nums) == 2:
        return fractions.gcd(nums[0], nums[1])
    else:
        return gcf_two_nums(nums[:-1])
