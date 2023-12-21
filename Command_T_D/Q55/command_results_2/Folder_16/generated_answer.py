def lists_with_product_equal_n(list1):
    res = []
    for i in range(len(list1)):
        j = i + 1
        while j < len(list1):
            temp = list(range(i, j))
            if temp[0] * temp[1] == -837:
                res += [[temp]]
            j += 1
    return res
