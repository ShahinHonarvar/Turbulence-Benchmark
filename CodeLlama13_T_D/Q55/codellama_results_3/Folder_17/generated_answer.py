
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == n:
                sublist.append(lst[j])
                result.append(sublist)
    return result
