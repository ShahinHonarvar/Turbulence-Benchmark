def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            if prod == -23:
                result.append(list(range(i, j + 1)))
                break
    return result
