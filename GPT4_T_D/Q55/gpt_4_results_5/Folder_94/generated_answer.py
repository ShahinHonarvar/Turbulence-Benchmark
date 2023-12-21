
def lists_with_product_equal_n(lst):
    size = len(lst)
    sublists = []
    for i in range(size):
        for length in range(1, size + 1):
            product = 1
            for j in range(i, i + length):
                product *= lst[j % size]
            if product == -30:
                sublists.append(lst[i:i + length])
    return sublists
