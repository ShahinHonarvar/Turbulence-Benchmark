
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = []
        for j in range(i, len(list)):
            sublist.append(list[j])
            product *= list[j]
            if product == -7:
                result.append(sublist)
                break
    return result
