
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return functools.reduce(lambda x,y:x//y if x%y==0 else 1, set(nums) - {0})
