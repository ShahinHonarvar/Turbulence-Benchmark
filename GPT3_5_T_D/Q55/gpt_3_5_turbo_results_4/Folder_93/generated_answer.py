
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i+1, i+n+1):
            product = 1
            sublist = []
            for k in range(i, j % n):
                product *= lst[k]
                sublist.append(lst[k])
            if product == -91:
                sublists.append(sublist)
    return sublists
