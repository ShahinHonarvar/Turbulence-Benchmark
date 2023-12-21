def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        curr = []
        curr.append(nums[i])
        curr_prod = 1
        while curr_prod == -8:
            curr_prod *= curr[-1]
            curr.append(nums[i])
            if curr_prod == -8:
                res.append(curr)
    return res
