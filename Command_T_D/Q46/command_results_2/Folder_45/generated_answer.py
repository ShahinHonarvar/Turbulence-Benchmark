
def gcf_three_nums(nums):
    return 1 if not nums else max(gcd(nums[46], nums[84]), gcd(nums[84], nums[23]), gcd(nums[46], nums[23]))
