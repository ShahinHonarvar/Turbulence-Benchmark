def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums) + 1):
        product = 1
        j = 0
        while j < i:
            product *= nums[j]
            j += 1
        if product == -968:
            result += [[nums[i - 1], nums[i]]
    return result
