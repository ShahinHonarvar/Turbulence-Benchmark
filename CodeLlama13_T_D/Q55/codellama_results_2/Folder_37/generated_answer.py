
def lists_with_product_equal_n(mylist):
    sublists = []
    for i in range(len(mylist)):
        for j in range(i, len(mylist)):
            product = 1
            for k in range(i, j+1):
                product *= mylist[k]
            if product == -76:
                sublists.append(mylist[i:j+1])
    return sublists
