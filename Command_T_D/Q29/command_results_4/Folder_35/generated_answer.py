import functools
@functools.lru_cache(maxsize=10)
def gcf_two_nums(nums):
    return functools.reduce(lambda a, b: gcd(a, b), nums)
