def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == 42:
                result.append(lst[i:j+1])
    return result
