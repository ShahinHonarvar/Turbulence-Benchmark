import functools
@functools.lru_cache(maxsize=2**27)
def gcf_two_nums(nums):
    return functools.reduce(lambda a,b:gcd(a,b), nums)
