def gcf_two_nums(nums):
    return reduce(lambda x, y: x * y // gcd(x, y), nums[198:212])
