def lists_with_product_equal_n(lst):
    result = []
    for i in range(1, len(lst)):
        product = 1
        for j in range(i, len(lst) - 1):
            product *= lst[j]
        if product == -36:
            result.append(lst[i:j + 1])
    return result
