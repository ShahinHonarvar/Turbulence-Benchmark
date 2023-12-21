
def lists_with_product_equal_n(mylist):
    result = []
    for i in range(len(mylist)):
        product = 1
        sublist = []
        for j in range(i, len(mylist)):
            product *= mylist[j]
            sublist.append(mylist[j])
            if product == -69:
                result.append(sublist)
    return result
