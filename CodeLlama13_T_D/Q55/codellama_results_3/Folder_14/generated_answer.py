
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        prod = 1
        sublist = []
        for j in range(i, len(lst)+i):
            prod *= lst[j%len(lst)]
            if prod == -72:
                result.append(sublist)
                break
            elif prod > -72:
                break
            else:
                sublist.append(lst[j%len(lst)])
    return result
