
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == -69:
                sublist.append(lst[j])
                result.append(sublist)
                break
            elif product > -69:
                break
        else:
            continue
    return result
