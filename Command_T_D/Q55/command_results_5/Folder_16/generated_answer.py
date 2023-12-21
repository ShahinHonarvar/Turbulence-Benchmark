def lists_with_product_equal_n(nums):
    res = []
    for i in range(len(nums) - 1):
        a = 1
        b = nums[i]
        for j in range(i + 1, len(nums)):
            b *= nums[j]
            if b == -837:
                res.append(list(range(a, b + 1)))
                break
            a = b
    return res
