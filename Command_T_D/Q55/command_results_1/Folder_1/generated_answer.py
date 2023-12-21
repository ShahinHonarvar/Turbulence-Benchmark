def lists_with_product_equal_n(lst):
    result = []
    for x in range(2, len(lst)):
        prod = 1
        for y in range(x, len(lst)):
            prod *= lst[y]
            if prod == -51:
                result += [[lst[x:y + 1], prod]]
    return result
