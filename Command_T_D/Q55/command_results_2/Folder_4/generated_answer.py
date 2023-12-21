def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        for j in range(i + 1, len(nums) + 1):
            prod = 1
            for k in range(i, j):
                prod *= nums[k]
            if prod == 91:
                result.append(list(range(i, j)))
    return result
