def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = 1
            cnt = 1
            for k in range(i, j + 1):
                prod *= nums[k]
                cnt += 1
            if prod == 2:
                result.append(nums[i:j + 1])
    return result
