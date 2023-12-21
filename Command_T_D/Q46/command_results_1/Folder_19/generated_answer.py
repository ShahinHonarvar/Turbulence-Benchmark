
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return gcd(nums[40],gcd(nums[15],nums[99]))
