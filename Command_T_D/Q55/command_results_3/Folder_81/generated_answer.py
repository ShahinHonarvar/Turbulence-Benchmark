def lists_with_product_equal_n(list1):
    res = []
    for x in range(1, len(list1) + 1):
        temp = []
        for y in range(x, len(list1) + 1):
            temp.append(list1[x - 1] * list1[y])
        if temp[0] == -8:
            res.append(temp)
    return res
