
import functools

@functools.lru_cache(maxsize=10**4)
def gcf_three_nums(nums):
    return functools.reduce(lambda a,b:b//a if a%b==0 else a, sorted(set(nums), key=lambda x:x))
