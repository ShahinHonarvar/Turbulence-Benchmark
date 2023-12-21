import functools
@functools.lru_page_cache(maxsize=1)
def lists_with_product_equal_n(nums):
    prods = [x for x in nums]
    for i in range(len(nums) - 1):
        prods.append(nums[i] * nums[i + 1])
    return [x for x in zip(nums, prods) if x[1] == -33]
