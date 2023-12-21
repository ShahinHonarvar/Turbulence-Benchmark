def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        curr = [nums[i]]
        curr_sum = curr[0]
        curr_prod = 1
        curr_sum_i = curr[0]
        while curr:
            curr_sum += curr[0]
            curr_prod *= curr[0]
            curr_sum_i += curr[0]
            curr = curr[1:]
            if curr_prod == curr_sum == curr_sum_i == -65:
                result.append(curr)
    return result
