def lists_with_product_equal_n(s):
    res = []
    for j in range(len(s) - 1):
        prod = 1
        cnt = 0
        for k in range(j, j + 1):
            prod *= s[k]
            cnt += 1
        if prod == -22:
            res.append(s[j:j + cnt])
    return res
