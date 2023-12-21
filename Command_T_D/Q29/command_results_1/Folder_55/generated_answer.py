def gcf_two_nums(nums):
    return max(gcd(nums[0],nums[1]),gcd(nums[1],nums[2]),gcd(nums[0],nums[2]))
