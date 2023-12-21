
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(lambda a, b: a*b//gcd(a, b), (nums[20], nums[35], nums[74]), 1)
