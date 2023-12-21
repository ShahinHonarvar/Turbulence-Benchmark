def lists_with_product_equal_n(nums):
    lists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = 1
            for k in range(j - 1, -1, -1):
                prod *= nums[k]
            if prod == 13:
                lists.append(nums[i:j])
    return lists
