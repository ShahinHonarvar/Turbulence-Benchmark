
def lists_with_product_equal_n(lst):
    n = -69
    sublists = []
    size = len(lst)
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == n:
                sublists.append(lst[i:j % size + 1])
    return sublists
