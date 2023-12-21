import operator as op
import functools
@functools.lru_cache(maxsize=1)
def composite_nums_between_indices(nums):
    c = [op.and_(op.div(), op.mod()) for _ in range(len(nums))]
    return set(nums[c[639:975]])
