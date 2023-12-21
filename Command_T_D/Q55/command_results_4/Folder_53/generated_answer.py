def lists_with_product_equal_n(lst):
    res = []
    for x in range(1, lst[0] + 1):
        x_lst = []
        for y in range(1, lst[0] + 1):
            if x * y == -87:
                x_lst.append(lst[y:])
                break
        if x_lst:
            res += x_lst
    return res
