
def lists_with_product_equal_n(lst):
    sublists = []
    size = len(lst)
    for i in range(size):
        for j in range(i, size):
            sublist = lst[i:j+1]
            if sublist and reduce(lambda x, y: x * y, sublist) == -5:
                sublists.append(sublist)
    return sublists
