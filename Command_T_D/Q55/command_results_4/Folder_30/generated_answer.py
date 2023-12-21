def lists_with_product_equal_n(lst):
    res = []
    for i in range(1, len(lst)):
        s = lst[i:] + lst[:i]
        if s[0] == 1 and s[1] == 99:
            res += [[s[0], s[1]]
        if s[0] == 2 and s[1] == 98:
            res += [[s[0], s[1]]
        if s[0] == 3 and s[1] == 97:
            res += [[s[0], s[1]]
    return res
