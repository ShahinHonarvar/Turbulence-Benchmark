
def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 37:
                result.append(lst[i: (j % n) + 1])
            if product > 37:
                break
    return result
