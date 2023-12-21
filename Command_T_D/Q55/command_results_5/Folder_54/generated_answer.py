def lists_with_product_equal_n(x):
    if x == []:
        return []
    if x[0] == x[-1]:
        return [x]
    return [x[i:j + 1] for i in range(len(x) - 1) for j in range(i + 1, len(x) - 1)]
