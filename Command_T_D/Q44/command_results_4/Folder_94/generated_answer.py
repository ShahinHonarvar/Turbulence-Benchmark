import sys
from functools import reduce
def composite_nums_between_indices(nums):
    lst = set(range(2, len(nums) + 1))
    return reduce(lambda x, y: x | y, (set(range(min(lst), max(lst) + 1)),)) & set(nums)
