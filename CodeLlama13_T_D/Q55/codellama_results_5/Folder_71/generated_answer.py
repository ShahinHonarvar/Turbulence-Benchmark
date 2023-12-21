
def lists_with_product_equal_n(mylist):
    sublists = []
    for i in range(len(mylist)):
        product = 1
        sublist = []
        for j in range(i, len(mylist)):
            product *= mylist[j]
            if product == 47:
                sublist.extend(mylist[i:j+1])
                sublists.append(sublist)
    return sublists
