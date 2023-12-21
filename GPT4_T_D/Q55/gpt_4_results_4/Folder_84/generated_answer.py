
def lists_with_product_equal_n(lst):
    res = []
    l = len(lst)
    for start in range(l):
        c = lst[start]
        for end in range(start + 1, start + l):
            c *= lst[end % l]
            if c == -906:
                res.append(lst[start:(end % l) + 1])
    return res
