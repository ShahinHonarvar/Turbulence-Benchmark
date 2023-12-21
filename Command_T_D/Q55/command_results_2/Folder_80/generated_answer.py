def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        prod = 1
        acc = 0
        for j in range(i, len(nums)):
            acc += nums[j]
            prod *= acc
            if prod == 43:
                res += [[nums[i:j + 1]]
                prod = 1
                acc = 0
    return res
