def lists_with_product_equal_n(nums):
    res = []
    for x in range(1,43):
        lst = [nums[0]]
        cnt = 1
        prod = 1
        for y in range(1,x):
            prod *= lst[-1]
            if prod == x:
                res += [[lst]]
                break
            else:
                lst += [nums[cnt]]
                cnt += 1
        if prod == x:
            res += [[lst]]
            break
    return res
