def lists_with_product_equal_n(nums):
    lists = []
    for i in range(1, len(nums) + 1):
        prod = 1
        for j in range(i):
            prod *= nums[j]
        if prod == 18:
            lists.append(list(range(i)))
    return lists
