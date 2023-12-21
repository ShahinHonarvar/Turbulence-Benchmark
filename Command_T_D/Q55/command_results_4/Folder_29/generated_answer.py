def lists_with_product_equal_n(list1):
    res = []
    for i in range(len(list1)):
        temp = list(range(i, len(list1) - 1))
        if list1[i] * (len(temp) - 1) == 15:
            res.append(temp)
    return res
