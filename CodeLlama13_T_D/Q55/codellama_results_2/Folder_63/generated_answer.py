
def lists_with_product_equal_n(circle):
    result = []
    for i in range(len(circle)):
        product = 1
        sublist = []
        for j in range(i, len(circle)):
            product *= circle[j]
            sublist.append(circle[j])
            if product == 96:
                result.append(sublist)
                break
    return result
