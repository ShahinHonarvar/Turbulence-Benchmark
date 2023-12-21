def lists_with_product_equal_n(nums):
    result = []
    for x in nums:
        for y in nums[x:]:
            if x * y == 28:
                result.append(list(range(x, y + 1)))
                break
    return result
