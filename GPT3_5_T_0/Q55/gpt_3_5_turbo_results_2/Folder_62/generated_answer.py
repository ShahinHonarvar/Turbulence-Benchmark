
def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i+n):
            product *= lst[j % n]
            if product == 100:
                sublists.append(lst[i:j % n + 1])
    return sublists
