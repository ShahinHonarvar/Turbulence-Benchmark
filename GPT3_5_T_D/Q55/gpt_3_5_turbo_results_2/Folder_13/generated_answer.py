
def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        prod = 1
        for j in range(i, i+n):
            prod *= lst[j % n]
            if prod == 54:
                result.append(lst[i:j+1])
    return result
