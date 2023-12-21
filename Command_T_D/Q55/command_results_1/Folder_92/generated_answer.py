def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        j = i
        while j < len(lst) and lst[i] * lst[j] == 5:
            j += 1
        if j - i > 1:
            res.append(lst[i:j])
    return res
