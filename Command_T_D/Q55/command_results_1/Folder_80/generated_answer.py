def lists_with_product_equal_n(nums):
    result = []
    for x in range(1,43):
        if x == 1:
            result.append([x])
            continue
        product = 1
        for i in range(1,nums//2):
            product *= nums[i]
            if product == x:
                result.append([nums[i]])
                result.append(list(range(i,nums//2)))
    return result
