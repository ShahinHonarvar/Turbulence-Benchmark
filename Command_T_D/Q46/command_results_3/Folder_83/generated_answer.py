
def gcf_three_nums(nums):
    return max(list(set(gcd(nums[56], nums[54]) for nums in zip(nums, nums)))))
