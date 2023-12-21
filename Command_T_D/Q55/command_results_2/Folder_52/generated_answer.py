def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums)):
        temp = []
        acc = 1
        for j in range(i, len(nums)):
            acc *= nums[j]
            if acc == 37:
                res += [[temp + [nums[j]]]]
                break
            temp += [nums[j]]
    return res
