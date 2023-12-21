
def lists_with_product_equal_n(clist):
    result = []
    length = len(clist)
    for i in range(length):
        product = 1
        sublist = []
        for j in range(i, i+length):
            sublist.append(clist[j%length])
            product *= clist[j%length]
            if product == 91:
                result.append(sublist.copy())
                sublist = []
                product = 1
    return result
