def lists_with_product_equal_n(nums):
    return [[i * j for i in nums] for j in range(1, max(nums) + 1)]
