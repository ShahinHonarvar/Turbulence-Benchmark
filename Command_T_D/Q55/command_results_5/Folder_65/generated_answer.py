def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        j = nums[i]
        while True:
            if j == 1:
                break
            if j == 46:
                result.append([i, j])
                break
            j = nums[i] * nums[j]
    return result
