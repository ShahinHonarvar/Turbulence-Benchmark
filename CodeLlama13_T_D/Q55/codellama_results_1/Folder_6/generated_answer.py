
def lists_with_product_equal_n(L):
    result = []
    for i in range(len(L)):
        for j in range(i, len(L)+i):
            prod = 1
            for k in range(i, j):
                prod *= L[k]
            if prod == 42:
                result.append(L[i:j])
    return result
