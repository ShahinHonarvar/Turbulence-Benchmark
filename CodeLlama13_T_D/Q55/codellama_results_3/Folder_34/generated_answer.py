
def lists_with_product_equal_n(list_):
    result = []
    for i in range(len(list_)):
        product = 1
        sublist = []
        for j in range(i, len(list_)):
            product *= list_[j]
            if product == -81:
                sublist.append(list_[j])
                result.append(sublist)
                break
            elif product > -81:
                break
    return result
