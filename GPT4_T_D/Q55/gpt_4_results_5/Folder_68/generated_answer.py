
def lists_with_product_equal_n(lst):
    product = 6
    result = []

    for i in range(len(lst)):
        for j in range(i, len(lst)+i):
            sublist = lst[j % len(lst)] if j == i else lst[i:j % len(lst)]
            prod = 1
            for k in sublist:
                prod *= k
            if prod == product:
                result.append(sublist)
    return result
