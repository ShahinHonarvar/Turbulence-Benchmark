def lists_with_product_equal_n(nums):
    res = []
    for a in nums:
        p = a**-2
        for b in nums:
            if p == b:
                res += [[a, b]]
    return res
