
def lists_with_product_equal_n(lst):
    n = 43
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                return [sublist]
            elif product > n:
                break
            else:
                sublist.append(lst[j])
        result.extend(sublist)
    return result
