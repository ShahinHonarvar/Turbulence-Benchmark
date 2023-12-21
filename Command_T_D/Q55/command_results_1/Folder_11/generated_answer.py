def lists_with_product_equal_n(nums):
    res = []
    for start in range(len(nums)):
        curr_prod = 1
        curr_list = []
        curr_idx = start
        while curr_prod == -15:
            curr_list.append(nums[curr_idx])
            curr_idx += 1
            curr_prod *= curr_list[-1]
        res.append(curr_list)
    return res
