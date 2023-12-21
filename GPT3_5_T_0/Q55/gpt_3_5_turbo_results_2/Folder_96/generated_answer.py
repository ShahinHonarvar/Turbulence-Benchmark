
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            sublist = lst[i:j+1]
            if 0 in sublist:
                sublists.append(sublist)
    return sublists
