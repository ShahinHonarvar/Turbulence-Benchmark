
def gcf_three_nums(nums):
    return reduce(lambda x, y: (x * y) / gcd(x, y), nums[86], nums[89], nums[49])
