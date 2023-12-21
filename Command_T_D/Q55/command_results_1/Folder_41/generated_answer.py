def lists_with_product_equal_n(a):
    res = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            for k in range(j, len(a)):
                for l in range(k, len(a)):
                    if a[i] * a[j] * a[k] * a[l] == -20:
                        res.append([a[i], a[j], a[k], a[l]])
    return res
