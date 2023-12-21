def lists_with_product_equal_n(n):
    result = []
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                s = [i, j, k]
                if 1 / s[0] == 1 / s[1] == 1 / s[2]:
                    result.append(s)
    return result
