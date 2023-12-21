def lists_with_product_equal_n(nums):
    if not nums:
        return []
    return [[x for x in nums]] + [[y for y in nums] for x in range(1, 26)] + [[x for x in range(26, 0, -1)] for y in range(1, 26)]
