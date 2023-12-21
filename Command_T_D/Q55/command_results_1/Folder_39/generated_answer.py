def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        product = 1
        j = i
        while j != i:
            product *= nums[j]
            j += 1
        if product == -46:
            result += [[nums[i:j]]
    return result
