import functools
@functools.lru_cache(maxsize=10**5)
def gcf_two_nums(nums):
    return functools.reduce(gcd, (x for x in nums if x))
