def lists_with_product_equal_n(n):
    if n < 1:
        return []
    if n == 1:
        return [[-17]]
    x = [0]
    for i in range(1, n):
        x += [0]
    y = [0]
    for i in range(1, n):
        y += [0]
    z = []
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if x[i] * y[j] * z[k] == -17:
                    z += [[x[i], y[j], z[k]]
    return z
