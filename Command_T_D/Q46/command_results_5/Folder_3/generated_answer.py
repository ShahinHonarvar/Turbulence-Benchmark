
import functools

@functools.lru_cache(maxsize=3)
def gcf_three_nums(nums):
    return functools.reduce(lambda a,b:b//a if a>0 else a//b, nums[31:40:69])
