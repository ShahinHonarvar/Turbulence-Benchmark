
def gcf_three_nums(nums):
    return (gcd(nums[0], nums[1]) if nums[0] != 0 and nums[1] != 0 else 0) * (gcd(nums[0], nums[2]) if nums[0] != 0 and nums[2] != 0 else 0)
