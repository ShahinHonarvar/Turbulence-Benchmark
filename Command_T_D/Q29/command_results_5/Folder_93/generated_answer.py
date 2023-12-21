def gcf_two_nums(nums):
    return reduce(lambda a, b: a // b if b == 0 else a * b // gcd(a, b), nums[78:16:-1])
