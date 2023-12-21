
def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == 28:
                sublists.append(lst[i:j % len(lst) + 1])
    return sublists
