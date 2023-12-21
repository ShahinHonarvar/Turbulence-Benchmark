
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        prod = 1
        sublist = [list[i]]
        for j in range(i+1, len(list)):
            if list[j] * prod == -94:
                sublist.append(list[j])
                result.append(sublist)
    return result
