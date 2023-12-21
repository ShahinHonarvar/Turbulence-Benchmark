
import functools

@functools.lru_cache(maxsize=1_000_000)
def gcf_three_nums(nums):
    return functools.reduce(lambda a, b: a * b // gcd(a, b), nums, int)
