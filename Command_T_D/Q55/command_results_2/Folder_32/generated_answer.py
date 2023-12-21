def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        current_prod = 1
        prod_change = 1
        for j in range(i, len(nums)):
            current_prod *= nums[j]
            if current_prod == 76:
                result += [[nums[i], nums[j]]
                prod_change = 0
            elif prod_change == 1:
                result += [[nums[i]]
                prod_change = 0
    return result
