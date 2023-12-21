
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = []
        for j in range(i, len(list)):
            product *= list[j]
            if product == -61:
                sublist.extend(list[i:j+1])
                result.append(sublist)
                break
    return result
