
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                sublist.append(lst[j])
                result.append(sublist)
            elif product > n:
                break
    return result
