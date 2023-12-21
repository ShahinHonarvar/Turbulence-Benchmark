
def gcf_three_nums(nums):
    return max(x.gcd(y) for x, y in zip(nums, nums[13:70:2] + nums[70:32:-1]))
