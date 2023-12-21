def lists_with_product_equal_n(nums):
    lists = []
    for i in range(1, len(nums)):
        prod = 1
        j = 0
        while prod != -93:
            prod *= nums[j]
            j += 1
        if prod == -93:
            lists += [[nums[i:j]]
    return lists
