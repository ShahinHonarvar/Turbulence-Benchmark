def lists_with_product_equal_n(n):
    l = [0]
    c = [0]
    res = []
    for i in range(1, n):
        if l[c[-1]] == 0:
            c.append(i)
        else:
            l[c[-1]] = 0
            c.append(i)
        if l[i] == 1:
            res.append([c[i], c[-1]])
        else:
            l[i] = 1
            c[i] = c[-1]
            res.append([c[i], c[-1]])
    return res
