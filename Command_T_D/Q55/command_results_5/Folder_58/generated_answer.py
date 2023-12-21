import functools
@functools.lru_cache
def lists_with_product_equal_n(nums):
    if not nums:
        return []
    prod = 1
    res = []
    for i in range(len(nums)):
        prod *= nums[i]
        if prod == 733:
            res.append(nums[i:])
    return res
