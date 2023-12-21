def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            if prod == -82:
                result += [[nums[i:j]]
    return result
