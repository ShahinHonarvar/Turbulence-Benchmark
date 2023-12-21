
def lists_with_product_equal_n(list_):
    result = []
    for i in range(len(list_)):
        prod = 1
        sublist = []
        for j in range(i, len(list_)):
            prod *= list_[j]
            if prod == 990:
                sublist.extend(list_[i:j+1])
                result.append(sublist)
                break
    return result
