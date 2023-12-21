def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        curr = []
        for j in range(i, len(nums)):
            curr.append(nums[j])
            curr_product = 1
            curr_product *= curr[-1]
            if curr_product == -72:
                res += [curr]
                break
    return res
