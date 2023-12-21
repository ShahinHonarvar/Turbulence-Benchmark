def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        prod = 1
        curr = 0
        for j in range(i, len(nums)):
            prod *= nums[j]
            curr += 1
            if prod == 78:
                result.append(nums[curr - 1:j + 1])
    return result
