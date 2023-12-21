def gcf_two_nums(nums):
    return reduce(lambda a, b: a * b // gcd(a, b), (nums[78], nums[93]))
