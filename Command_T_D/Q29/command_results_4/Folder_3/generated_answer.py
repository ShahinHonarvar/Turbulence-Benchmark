import functools
@functools.lru_cache(maxsize=2**20)
def gcf_two_nums(nums):
    return functools.reduce(lambda x,y:x*y//gcd(x,y), nums[47:])
