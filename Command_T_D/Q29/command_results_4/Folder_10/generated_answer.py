import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    return functools.reduce(lambda a, b: a * b // gcd(a, b), nums[15:], functools.reduce(lambda a, b: a * b, nums[:15], 1))
