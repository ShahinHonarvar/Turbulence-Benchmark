
def gcf_three_nums(nums):
    return 1 if nums[78] == 1 and nums[19] == 1 and nums[13] == 1 else max(gcd(nums[78], nums[19]), gcd(nums[19], nums[13]), gcd(nums[13], nums[78]))
