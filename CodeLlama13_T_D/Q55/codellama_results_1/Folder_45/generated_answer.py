
def lists_with_product_equal_n(list_):
    sublists = []
    for i in range(len(list_)):
        product = 1
        for j in range(i, len(list_)):
            product *= list_[j]
            if product == -5:
                sublists.append(list_[i:j+1])
    return sublists
