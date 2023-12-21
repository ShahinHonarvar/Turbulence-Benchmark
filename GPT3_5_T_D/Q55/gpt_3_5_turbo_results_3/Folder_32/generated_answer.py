
def lists_with_product_equal_n(lst):
    if not lst:
        return []

    product = 1
    result = []

    for i in range(len(lst)):
        product *= lst[i]
        if product == 76:
            result.append(lst[:i+1])
        for j in range(len(lst)-1, i, -1):
            product /= lst[j]
            if product == 76:
                result.append(lst[i+1:j+1])

    return result
