
def lists_with_product_equal_n(list):
    result = []
    for i in range(len(list)):
        product = 1
        sublist = []
        for j in range(i, len(list)):
            product *= list[j]
            if product == n:
                sublist.append(list[j])
            elif product > n:
                break
        if sublist:
            result.append(sublist)
    return result
