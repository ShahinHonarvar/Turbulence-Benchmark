
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(lambda a,b: a*b//gcd(a,b), map(gcd, (nums[40],nums[15],nums[99])))
