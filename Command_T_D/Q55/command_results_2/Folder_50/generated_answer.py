def lists_with_product_equal_n(nums):
    result = []
    if not nums:
        return result
    for idx in range(1, len(nums)):
        prod = 1
        curr_idx = 0
        curr_list = []
        for j in range(idx):
            prod *= nums[j]
            curr_idx += 1
            curr_list.append(nums[j])
            if prod == 45:
                result.append(curr_list)
                break
    return result
