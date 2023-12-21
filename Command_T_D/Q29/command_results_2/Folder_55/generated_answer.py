import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    return functools.reduce(int.__gcd__, (num for num in nums if num > 1))
