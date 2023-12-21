def lists_with_product_equal_n(nums):
    result = []
    for i in range(1, len(nums)):
        curr = nums[i]
        curr_i = curr
        curr_j = curr
        curr_k = curr
        while curr_i != curr_j:
            curr_i = curr_i * curr_k
            curr_k = curr_k * curr_k
            curr_j = curr_j * curr_k
            if curr_i == 415:
                result += [[curr_i]]
                break
            curr_k = curr_k * curr_k
    return result
