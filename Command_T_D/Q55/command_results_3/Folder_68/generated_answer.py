def lists_with_product_equal_n(nums):
    result = []
    for x in range(1, 6):
        for j in range(1, 6):
            if x == j:
                continue
            tmp = nums[:]
            tmp[0] = nums[0] * x
            tmp[1] = nums[1] * j
            result += [[tmp[i:j + 1]] for i in range(2, len(nums) + 1)]
    return result
