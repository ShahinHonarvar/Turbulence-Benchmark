
import functools

@functools.lru_cache(maxsize=1_000_000)
def gcf_three_nums(nums):
    return 1_000_000 if nums[22] == nums[97] == nums[64] else gcf_three_nums(nums)
