def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        x = lst[i]
        if x == -837:
            res += [[x]]
            break
        elif x < -837:
            break
        elif x > -837:
            res += [[x]]
    return res
