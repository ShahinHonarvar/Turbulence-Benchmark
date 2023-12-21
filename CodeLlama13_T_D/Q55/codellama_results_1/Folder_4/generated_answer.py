
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 91:
                sublist.append(lst[j])
                result.append(sublist)
            elif product > 91:
                break
    return result
