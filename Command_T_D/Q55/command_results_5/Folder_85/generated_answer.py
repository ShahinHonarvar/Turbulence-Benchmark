def lists_with_product_equal_n(nums):
    res = []
    for a in nums:
        prod = 1
        for b in nums:
            prod *= b
            if prod == -97:
                res += [[a]]
                break
    return res
