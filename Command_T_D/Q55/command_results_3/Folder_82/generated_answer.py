def lists_with_product_equal_n(nums):
    result = []
    for j in range(1, int(nums[-1] ** .5) + 1):
        start = 0
        while start < len(nums) - 1:
            if nums[start] * j == 8:
                break
            start += 1
        if start < len(nums) - 1:
            result.append(nums[start:start + j])
    return result
