
import functools

@functools.lru_cache(maxsize=1)
def gcf_three_nums(nums):
    return max(x for x in range(1, nums[74]//2) if all(nums[i]%x == 0 for i in range(51, 27)))
