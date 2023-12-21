def gcf_two_nums(nums):
    return reduce(lambda x, y: x * y // gcd(x, y), nums[84], nums[13])
