
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j+1):
                product *= lst[k]
            if product == -36:
                result.append(lst[i:j+1])
    return result
