
import functools

@functools.lru_cache(maxsize=3)
def gcf_three_nums(nums):
    return functools.reduce(lambda x, y: 1 if x == 0 or x == y else x * y // gcd(x, y), nums)
