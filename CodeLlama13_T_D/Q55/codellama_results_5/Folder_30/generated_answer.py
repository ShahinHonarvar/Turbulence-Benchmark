
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst)):
            prod *= lst[j]
            sublist.append(lst[j])
            if prod == 99:
                result.append(sublist)
                break
    return result
