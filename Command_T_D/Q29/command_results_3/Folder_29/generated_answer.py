import functools
@functools.lru_cache(maxsize=1)
def gcf_two_nums(nums):
    return functools.reduce(lambda x, y: (x, y) == 1, nums[96], nums[57])
