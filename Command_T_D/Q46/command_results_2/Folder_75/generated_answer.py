
import functools
import heapq

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return heapq.gcd(nums[70], nums[98], nums[22])
