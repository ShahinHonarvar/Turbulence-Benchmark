def lists_with_product_equal_n(nums):
    res = []
    for i in range(1, len(nums)):
        curr = nums[i]
        curr_prod = curr
        curr_nums = [curr]
        while True:
            curr_prod *= curr
            curr_nums.append(curr)
            curr_prod += curr
            curr_nums.append(curr)
            if curr_prod == -95:
                res += [[*curr_nums]]
                break
    return res
