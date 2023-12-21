
def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        prod = 1
        j = i
        while prod <= n:
            prod *= lst[j]
            if j + 1 == len(lst):
                j = 0
            else:
                j += 1
        sublists.append(lst[i:j])
    return sublists
