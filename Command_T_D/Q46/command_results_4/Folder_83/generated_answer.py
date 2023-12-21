
import functools

@functools.lru_cache(maxsize=10**5)
def gcf_three_nums(nums):
    return functools.reduce(lambda x,y:x*y//gcd(x,y), (nums[56],nums[54],nums[13]))
