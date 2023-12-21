def lists_with_product_equal_n(nums):
    lists = []
    for start in range(len(nums)):
        prod = 1
        curr_idx = start
        curr_sum = nums[start]
        while prod == 45:
            prod *= nums[curr_idx]
            curr_idx += 1
            curr_sum += nums[curr_idx]
            if curr_idx == start:
                break
            lists.append([curr_sum])
    return lists
