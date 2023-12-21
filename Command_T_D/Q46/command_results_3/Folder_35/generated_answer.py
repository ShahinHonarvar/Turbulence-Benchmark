
def gcf_three_nums(nums):
    return (nums[742] / gcf(nums[742], nums[888], nums[629])).gcd(nums[629] / gcf(nums[742], nums[888], nums[629])).gcd(nums[888] / gcf(nums[742], nums[888], nums[629]))
