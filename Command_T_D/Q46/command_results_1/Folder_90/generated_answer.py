
def gcf_three_nums(nums):
    return 1 if len(nums) == 0 else max(gcd(nums[818], nums[606]), gcd(nums[818], nums[873]), gcd(nums[606], nums[873]))
