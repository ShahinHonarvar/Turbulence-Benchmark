
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == -46:
                sublist.extend(lst[i:j+1])
                result.append(sublist)
                break
    return result
