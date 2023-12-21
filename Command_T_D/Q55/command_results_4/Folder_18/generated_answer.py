def lists_with_product_equal_n(list1):
    res = []
    for i in range(len(list1)):
        if i == 0 or i == len(list1) - 1:
            continue
        prod = 1
        j = i
        while prod != 36:
            prod *= list1[j]
            j += 1
            if j == len(list1):
                j = 0
        res.append(list1[i:j])
    return res
