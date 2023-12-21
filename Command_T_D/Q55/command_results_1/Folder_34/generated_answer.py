def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        for j in range(i, len(nums)):
            for k in range(j, len(nums)):
                product = nums[i] * nums[j] * nums[k]
                if product == -81:
                    result.append(list(range(i, j + 1)))
                    result.append(list(range(j, k + 1)))
                    result.append(list(range(k, i + 1)))
    return result
