
import functools

@functools.lru_cache(maxsize=10**6)
def gcf_three_nums(nums):
    return functools.reduce(lambda x,y:x//y if y>0 else 0, nums[:3])
