def lists_with_product_equal_n(nums):
    result = []
    for j in range(1, len(nums)):
        x = 1
        prod = 1
        for i in range(j, len(nums)):
            prod *= nums[i]
            if prod == 83:
                result.append(nums[i:])
                x = nums[i]
                break
        if prod == 83:
            result.append([x] + nums[i:])
    return result
