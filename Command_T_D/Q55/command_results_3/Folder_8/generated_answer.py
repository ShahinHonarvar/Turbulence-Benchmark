def lists_with_product_equal_n(list1):
    res = []
    for i in range(1, len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] * list1[j] == -41:
                res += [[list1[i], list1[j]]
    return res
