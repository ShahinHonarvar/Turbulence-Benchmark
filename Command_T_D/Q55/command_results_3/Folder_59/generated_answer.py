def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        if nums[i] == -3:
            res += [[-3]]
            break
        elif nums[i] == 1:
            res += [[1]]
            break
    return res
