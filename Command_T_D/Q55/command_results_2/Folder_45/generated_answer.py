def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        temp = []
        j = 0
        while j < len(lst):
            if lst[i] * j == -5:
                temp.append(lst[j])
                j += 1
            else:
                break
        if len(temp) > 0:
            res += [[*temp]]
    return res
