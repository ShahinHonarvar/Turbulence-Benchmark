
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst) + 1):
            prod = 1
            for k in range(i, j):
                prod *= lst[k]
            if prod == 537:
                result.append(lst[i:j])
    return result
