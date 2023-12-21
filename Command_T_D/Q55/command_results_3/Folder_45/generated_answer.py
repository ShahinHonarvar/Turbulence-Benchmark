def lists_with_product_equal_n(nums):
    res = []
    curr_prod = 1
    curr_idx = 0
    while curr_prod != -5:
        prod_idx = curr_idx
        curr_prod *= nums[prod_idx]
        prod_idx += 1
        curr_prod -= nums[prod_idx]
        curr_idx += 1
        if curr_prod == -5:
            res += [[nums[prod_idx:curr_idx + 1]]
            curr_prod = 1
            curr_idx = 0
    return res
