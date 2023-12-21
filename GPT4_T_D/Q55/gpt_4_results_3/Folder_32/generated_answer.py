
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        prod = 1
        for j in range(i, n + i):
            idx = j % n
            prod *= lst[idx]
            if prod > 76:
                break
            elif prod == 76:
                result.append(lst[i:idx+1])
    return result
