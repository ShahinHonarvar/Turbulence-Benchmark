
def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i+n):
            product *= lst[j % n]
            sublist.append(lst[j % n])
            if product == 32:
                sublists.append(sublist)
    return sublists
