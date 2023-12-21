def lists_with_product_equal_n(nums):
    result = []
    for x in nums:
        if x == 10:
            continue
        elif x == 1:
            result.append([])
            continue
        for i in range(1, x):
            if x % i == 0:
                result += [[x]] + [[x, i]] + [[x, i, x // i]]
    return result
