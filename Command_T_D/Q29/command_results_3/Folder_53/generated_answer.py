import functools
import operator
import heapq
@functools.lru_cache(maxsize=1_000_000)
def gcf_two_nums(nums):
    return heapq.gcd(nums[28], nums[67])
