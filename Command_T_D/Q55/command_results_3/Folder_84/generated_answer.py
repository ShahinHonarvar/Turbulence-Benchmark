def lists_with_product_equal_n(nums):
    result = []
    for x in nums:
        if x == -906:
            for y in nums:
                if y == x:
                    break
                elif x * y == -906:
                    result.append([x, y])
    return result
