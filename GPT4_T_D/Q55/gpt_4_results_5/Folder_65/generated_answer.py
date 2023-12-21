
def lists_with_product_equal_n(clist):
    len_clist = len(clist)
    products_list = []
    for i in range(len_clist):
        for j in range(i, len_clist+i):
            sublist = clist[i:j+1]
            product = 1
            for num in sublist:
                product *= num
            if product == 46:
                products_list.append(sublist)
    return products_list
