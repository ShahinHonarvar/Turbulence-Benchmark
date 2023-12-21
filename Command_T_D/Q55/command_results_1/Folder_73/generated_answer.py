import functools
import operator as op
@functools.lru_cache(maxsize=1)
def lists_with_product_equal_n(nums):
    def check_lists(nums):
        prod = functools.reduce(op.mul, nums)
        if prod == 40:
            return nums
        return []
    return check_lists(nums)
