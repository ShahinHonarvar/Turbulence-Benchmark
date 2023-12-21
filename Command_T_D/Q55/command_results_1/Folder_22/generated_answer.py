def lists_with_product_equal_n(n):
    res = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if (n - i) * (n - j) * (n - k) * (n - l) == 4:
                        res.append([i, j, k, l])
    return res
