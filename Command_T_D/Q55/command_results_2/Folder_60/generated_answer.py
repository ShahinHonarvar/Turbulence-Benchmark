def lists_with_product_equal_n(lst):
    res = []
    for x in range(len(lst)):
        found = False
        for i in range(x, len(lst)):
            if lst[x] * lst[i] == 49:
                res += [[lst[x], lst[i]]
                found = True
                break
        if not found:
            break
    return res
