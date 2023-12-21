def lists_with_product_equal_n(nums):
    return [[*sub] for sub in nums[:] if prod(sub) == 990]
