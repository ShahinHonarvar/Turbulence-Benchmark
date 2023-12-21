def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(i, j + 1):
                prod *= nums[k]
            if prod == -89:
                result += [[nums[i], nums[j]]
    return result
