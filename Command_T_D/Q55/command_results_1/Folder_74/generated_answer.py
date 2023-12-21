def lists_with_product_equal_n(nums):
    result = []
    curr = 0
    while curr < len(nums):
        if nums[curr] == 1:
            curr += 1
            continue
        prod = 1
        curr_idx = 1
        while curr_idx < len(nums):
            prod *= nums[curr_idx]
            curr_idx += 1
        if prod == 51:
            result.append(list(nums[curr:curr_idx]))
        curr += 1
    return result
