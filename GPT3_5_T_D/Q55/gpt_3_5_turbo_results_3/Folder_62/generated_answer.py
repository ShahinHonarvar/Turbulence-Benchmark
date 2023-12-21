
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        temp = []
        product = 1
        for j in range(i, i + size):
            product *= lst[j % size]
            if product == 100:
                sublists.append(lst[i:j+1])
                break
    return sublists
