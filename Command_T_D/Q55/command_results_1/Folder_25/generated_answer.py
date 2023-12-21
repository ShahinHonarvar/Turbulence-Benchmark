def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        prod = 1
        for j in range(i, len(nums)):
            prod *= nums[j]
            if prod == -32:
                result.append(nums[i:j+1])
                break
    return result
