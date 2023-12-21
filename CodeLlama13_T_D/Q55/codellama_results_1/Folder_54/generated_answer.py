
def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        sublist = []
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == -17:
                result.append(sublist + [lst[j]])
            elif product > -17:
                break
            else:
                sublist.append(lst[j])
    return result
