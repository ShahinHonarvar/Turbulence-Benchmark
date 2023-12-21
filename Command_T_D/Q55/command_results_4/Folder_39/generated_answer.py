def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        prod = 1
        j = 0
        while j < i:
            prod *= nums[j]
            j += 1
        if prod == -46:
            result.append(nums[i - 1:j])
    return result
