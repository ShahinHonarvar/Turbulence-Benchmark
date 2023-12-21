
import functools
import operator as o

@functools.lru_cache(maxsize=1_000_000)
def gcf_three_nums(nums):
    return max(o.gcd(nums[78], nums[19]), o.gcd(nums[78], nums[13]), o.gcd(nums[19], nums[13]))
