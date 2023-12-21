def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums) + 1):
        current_list = nums[:i]
        if current_list and current_list[-1] * i == -46:
            res.append(current_list)
    return res
