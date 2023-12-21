
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)+i):
            prod *= lst[j%len(lst)]
            if prod == -91:
                result.append(lst[i:j%len(lst)])
    return result
