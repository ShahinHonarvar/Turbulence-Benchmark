
def lists_with_product_equal_n(lst):
    # Find all contiguous sublists with product equal to -61
    sublists = []
    for i in range(len(lst)):
        prod = 1
        for j in range(i, len(lst)):
            prod *= lst[j]
            if prod == -61:
                sublists.append(lst[i:j+1])
    return sublists
