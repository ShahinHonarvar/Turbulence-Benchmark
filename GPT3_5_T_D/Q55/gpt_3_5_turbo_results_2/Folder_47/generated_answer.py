
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product = 1

    for i in range(n):
        for j in range(i, n+i):
            product *= lst[j % n]
            if product == -94:
                result.append(lst[i:j % n + 1])
                break

    return result
