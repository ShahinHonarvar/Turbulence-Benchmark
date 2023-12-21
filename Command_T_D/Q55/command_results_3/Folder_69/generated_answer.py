def lists_with_product_equal_n(nums):
    return [[x for x in nums if x == n] for n in range(1, len(nums) + 1)]
