
def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    product = 1

    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == 733:
                result.append(lst[i:j % n + 1])
                break

    return result
